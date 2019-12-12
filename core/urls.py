from django.urls import path
from core import views

urlpatterns = [
    path('', views.list_products, name='product_list'),
] 