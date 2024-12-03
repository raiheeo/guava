from rest_framework import serializers
from .models import UserProfile, ProductPhoto, Category, Product, Review, Rating



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['product_image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer()
    photos = ProductPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'photos',  'product_name', 'price', 'owner']


class ProductDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer()
    photos = ProductPhotoSerializer(many=True, read_only=True)
    category = CategorySerializer()
    created_date = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'check_original',
                  'photos', 'product_video', 'price', 'owner', 'created_date']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'






