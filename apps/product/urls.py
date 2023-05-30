from django.urls import path

from .views import ProductDetailView

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>/', ProductDetailView, name='product_detail'),
]
