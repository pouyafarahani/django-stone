from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.decorators.cache import cache_page

from apps.product.models import TombstoneModel


@cache_page(600)
def home_view(request):
    try:
        tombstone = TombstoneModel.objects.filter(group='tombstone')[:4]
        inscription = TombstoneModel.objects.filter(group='inscription')[:4]
        sandblast = TombstoneModel.objects.filter(group='sandblast')[:4]
        wholesale = TombstoneModel.objects.filter(group='wholesale')[:4]
        return render(request, 'home/home.html',
                      {'tombstone': tombstone, 'inscription': inscription, 'sandblast': sandblast,
                       'wholesale': wholesale})

    except ConnectionError:
        HttpResponse('سایت در حال بروزرسانی میباشد. لطفا کمی بعد دوباره تلاش کنید')
