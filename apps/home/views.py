from django.shortcuts import render
from django.views import View
from django.core.cache import cache

from apps.product.models.product import ProductModel


class HomeView(View):
    def get(self, request):
        products = cache.get('home_products')
        if not products:
            products = list(ProductModel.objects.order_by('-id')[:8])
            cache.set('home_products_queryset', products, 60 * 15)  # cache queryset for 15 minutes
        return render(request, 'home/home.html', {'products': products})
