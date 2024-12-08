from django.db import models
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from phonenumber_field.modelfields import PhoneNumberField



class UserProfile(models.Model):
    objects = None
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    user_image = models.ImageField(upload_to='user_image/')
    age = models.PositiveSmallIntegerField(verbose_name='age')
    phone_number = PhoneNumberField(null=True, blank=True, region='KZ')
    register_date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('gold', 'gold'),
        ('silver', 'silver'),
        ('bronze', 'bronze'),
        ('simple', 'simple'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=16, default='simple')

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=44)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=34)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    price = models.PositiveIntegerField()
    check_original = models.BooleanField(default=True)
    product_video = models.FileField(upload_to='product_videos/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True )

    def __str__(self):
        return self.product_name

    def get_avg_rating(self):
        rating = self.get_avg_rating().all()
        if rating.exists():
            return  round(sum(i.stars for i in rating) / rating.count, 1)
        return 0

    def get_count_people(self):
        rating =self.get_count_people().all()
        if rating.exists():
            return rating.count()
        return 0

class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])


class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='photos')
    product_image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.product}'


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f'{self.user} rated {self.product} with {self.stars} stars'

class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.product}'


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f"Cart {self.id}"

def total_price(self):
    total = sum(item.total_price() for item in self.items.all())
    discount = self.get_discount()
    return total * (1 - discount)


def get_discount(self):
    discounts = {
        'gold': 0.75,
        'silver': 0.5,
        'bronze': 0.25,
        'simple': 0,
    }
    return discounts.get(self.status, 0)


def __str__(self):
    return f"Cart {self.id}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

