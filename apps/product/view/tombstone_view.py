from django.views.generic import ListView, DetailView

from apps.product.models.tombstone import TombstoneModel


class TombstoneListView(ListView):
    model = TombstoneModel
    context_object_name = 'products'
    template_name = 'product/product_list.html'
    paginate_by = 18

    def get_queryset(self):
        return TombstoneModel.objects.only('name', 'price', 'image', 'discount')


class TombstoneDetailView(DetailView):
    model = TombstoneModel
    template_name = 'product/product_detail.html'
    context_object_name = 'products'
