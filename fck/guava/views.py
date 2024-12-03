from .models import UserProfile, Product, ProductPhoto, Category, Review, Rating
from .models import Product
from .serializers import (
    UserProfileSerializer, ProductListSerializer, ProductDetailSerializer,
    ProductPhotoSerializer, CategorySerializer, ReviewSerializer, RatingSerializer
)
from rest_framework import viewsets
from .serializers import ProductListSerializer, ProductDetailSerializer


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

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


class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer



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







