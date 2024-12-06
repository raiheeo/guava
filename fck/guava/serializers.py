from unicodedata import category
from rest_framework import serializers
from .models import UserProfile, ProductPhoto, Category, Product, Review, Rating



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']

class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['product_image']

class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']



class ProductListSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer()
    photos = ProductPhotoSerializer(many=True, read_only=True)
    get_avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    def get_queryset(self):
        queryset = Product.objects.all().select_related('owner', 'category').prefetch_related('photos')
        return queryset

    class Meta:
        model = Product
        fields = ['id', 'photos',  'product_name', 'price', 'owner', 'get_avg_rating', 'get_count_people']


    def get_avg_rating(self,obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people

class CategorySerializer(serializers.ModelSerializer):
    products = ProductListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    class Meta:
        model = Rating
        fields = ['user', 'stars']


class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer
    date = serializers.DateField(format('%d-%m-%Y'))
    class Meta:
        model = Review
        fields = ['user', 'text', 'date']


class ProductDetailSerializer(serializers.ModelSerializer):
    owner = UserProfileSerializer()
    photos = ProductPhotoSerializer(many=True, read_only=True)
    category = CategorySimpleSerializer()
    created_date = serializers.DateField(format='%d-%m-%Y')
    ratings = RatingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'check_original',
                  'photos', 'product_video', 'price', 'owner', 'created_date', 'ratings', 'reviews']







