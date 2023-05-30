from django.shortcuts import render

from apps.product.models.product import ProductModel


def HomeView(request):
    products = ProductModel.objects.all().order_by('-id')[:8]
    return render(request, 'home/home.html', {'products': products})
