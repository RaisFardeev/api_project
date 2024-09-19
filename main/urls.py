from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('api/products/', views.product_list, name='product_list'),
    path('api/products/create/', views.product_create, name='product_create'),
]