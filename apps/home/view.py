from django.shortcuts import render

from apps.product.models import TombstoneModel


def home_view(request):
    tombstone = TombstoneModel.objects.all()
    return render(request, 'home/home.html', {'products': tombstone})
