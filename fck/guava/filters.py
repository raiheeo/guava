import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__category_name', lookup_expr='icontains')
    price = django_filters.RangeFilter()
    created_date = django_filters.DateFromToRangeFilter()
    product_name = django_filters.OrderingFilter(
        fields=('product_name',),
        label="Сортировка по названию",
        choices=[
            ('product_name', 'А-Я'),
            ('-product_name', 'Я-А'),
        ],
    )

    class Meta:
        model = Product
        fields = ['category', 'price', 'created_date']
