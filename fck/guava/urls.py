from django.urls import path
from .views import *



urlpatterns = [
    path('', ProductListViewSet.as_view({'get': 'list',
                                     'post': 'create'}), name='product_list'),

    path('<int:pk>/', ProductDetailViewSet.as_view({'get': 'retrieve',
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


]

