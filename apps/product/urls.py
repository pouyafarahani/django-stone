from django.urls import path

from .views import ProductDetailView, product_list


urlpatterns = [
    path('<slug:slug>/list/', product_list, name='product_list'),
    path('<int:pk>/detail/', ProductDetailView.as_view(), name='product_detail'),
]
