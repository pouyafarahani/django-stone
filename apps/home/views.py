from django.shortcuts import render
from django.views.generic import ListView

from apps.product.models.product import ProductModel


class HomeView(ListView):
    model = ProductModel
    context_object_name = 'products'
    template_name = 'home/home.html'
