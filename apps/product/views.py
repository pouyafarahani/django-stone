from django.views.generic import ListView, DetailView

from apps.product.models.product import ProductModel


class ProductDetailView(DetailView):
    model = ProductModel
    template_name = 'product/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductListView(ListView):
    model = ProductModel
    context_object_name = 'products'
    template_name = 'product/product_list.html'
    paginate_by = 18

    def get_queryset(self):
        return ProductModel.objects.only('name', 'price', 'image', 'discount')
