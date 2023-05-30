from django.contrib import messages
from django.shortcuts import render

from .forms import AboutForms
from ..product.models.product import ProductModel


def AboutView(request):
    return render(request, 'about/about.html')


def AboutForm(request):
    products = ProductModel.objects.all().order_by('-id')[:8]
    if request.method == 'POST':
        form = AboutForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد')
        else:
            messages.warning(request, 'لطفا اطلاعات رو به درستی پر کنید')

    return render(request, 'home/home.html', {'products': products})
