from django.urls import path

from .views import ProductDetailView, ProductListView

app_name = 'product'

urlpatterns = [
    path('detail/<int:pk>/', ProductDetailView, name='product_detail'),
    path('list/', ProductListView.as_view(), name='product_list'),
]
