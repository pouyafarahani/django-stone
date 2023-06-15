from django.shortcuts import render

from apps.product.models import TombstoneModel


def home_view(request):
    tombstone = TombstoneModel.objects.filter(group='tombstone')[:4]
    inscription = TombstoneModel.objects.filter(group='inscription')[:4]
    sandblast = TombstoneModel.objects.filter(group='sandblast')[:4]
    wholesale = TombstoneModel.objects.filter(group='wholesale')[:4]
    return render(request, 'home/home.html',
                  {'tombstone': tombstone, 'inscription': inscription, 'sandblast': sandblast, 'wholesale': wholesale})
