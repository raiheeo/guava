from django.shortcuts import render
from .models import UserProfile, Product, ProductPhoto, Category, Review, Rating
from .models import *
from .serializers import (
    UserProfileSerializer, ProductListSerializer, ProductDetailSerializer,
    ProductPhotoSerializer, CategorySerializer, ReviewSerializer, RatingSerializer
)
from rest_framework import viewsets
from .serializers import ProductListSerializer, ProductDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductListSerializer
from .filters import ProductFilter
from rest_framework import viewsets, permissions, status, generics
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.response import Response

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    search_fields = ['product_name']
    ordering_fields = ['price', 'date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):

        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductDetailSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        queryset = Product.objects.all()
        queryset = queryset.select_related('owner', 'category')
        queryset = queryset.prefetch_related('photos')

        return queryset


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductPhotoViewSet(viewsets.ModelViewSet):
    queryset = ProductPhoto.objects.all()
    serializer_class = ProductPhotoSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        cart = Cart.objects.create()
        serializer = self.get_serializer(cart)
        return Response(serializer.data)

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs): #Метод create создаёт пустую корзину и возвращает её данные.
        cart_id = request.data.get('cart')
        product_id = request.data.get('product')
        quantity = request.data.get('quantity', 1)

        if not cart_id or not product_id:
            return Response({"error": "Cart and Product are required."}, status=400)

        cart_item, created = CartItem.objects.get_or_create(
            cart_id=cart_id,
            product_id=product_id,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        serializer = self.get_serializer(cart_item)
        return Response(serializer.data)




