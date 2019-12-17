from django.urls import path
from core import views

urlpatterns = [
    path('', views.list_products, name='product_list'),
    path('<int:pk>', views.detail_product, name='product_detail'),
] 