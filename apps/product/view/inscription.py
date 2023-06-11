from django.views.generic import ListView, DetailView

from apps.product.models.inscription import InscriptionModel


class InscriptionListView(ListView):
    model = InscriptionModel
    context_object_name = 'inscription'
    template_name = 'product/product_list.html'
    paginate_by = 18

    def get_queryset(self):
        return InscriptionModel.objects.only('name', 'price', 'image', 'discount')


class InscriptionDetailView(DetailView):
    model = InscriptionModel
    template_name = 'product/product_detail.html'
    context_object_name = 'inscription'
