from django.shortcuts import render
from django.views.generic import DetailView
from django.http.response import HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from .models import TombstoneModel


@cache_page(200)
def product_list(request, slug):
    try:
        products = TombstoneModel.objects.filter(group=slug)
        return render(request, 'product/product_list.html', {'products': products})

    except ValueError:
        HttpResponse('این محصول وجود ندارد')


@method_decorator(cache_page(200), name='dispatch')
class ProductDetailView(DetailView):
    model = TombstoneModel
    template_name = 'product/product_detail.html'
    context_object_name = 'products'
