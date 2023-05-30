from django.shortcuts import render
from django.views.generic import ListView

from apps.product.models.product import ProductModel


def ProductDetailView(request, pk):
    products = ProductModel.objects.get(pk=pk)
    return render(request, 'product/product_detail.html', {'products': products})


class ProductListView(ListView):
    model = ProductModel
    context_object_name = 'products'
    template_name = 'product/product_list.html'
    paginate_by = 2
