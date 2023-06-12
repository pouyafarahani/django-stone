from django.views.generic import DetailView

from .models import TombstoneModel


class ProductDetailView(DetailView):
    model = TombstoneModel
    template_name = 'product/product_detail.html'
    context_object_name = 'products'
