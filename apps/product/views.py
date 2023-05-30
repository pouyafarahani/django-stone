from django.shortcuts import render

from .models import ProductModel


def ProductDetailView(request, pk):
    products = ProductModel.objects.get(pk=pk)
    return render(request, 'product/product_detail.html', {'products': products})
