from django.shortcuts import render

from apps.product.models import ProductModel


def HomeView(request):
    products = ProductModel.objects.all()
    return render(request, 'home/home.html', {'products': products})
