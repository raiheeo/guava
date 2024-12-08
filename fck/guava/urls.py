from django.urls import path
from .views import *
from django.conf import settings


urlpatterns = [
    path('', ProductListViewSet.as_view({'get': 'list',
                                     'post': 'create'}), name='product_list'),

    path('<int:pk>/', ProductListViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list',
                                          'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='category_detail'),
    path('user/', UserProfileViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='user_list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'delete': 'destroy'}), name='user_detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartViewSet.as_view({'get': 'list',
                                              'post': 'create'}), name='user_list'),
    path('cart/<int:pk>/', CartItemViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update',
                                                       'delete': 'destroy'}), name='user_detail'),
]
