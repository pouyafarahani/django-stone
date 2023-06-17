from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from .forms import AboutForms


@cache_page(400)
def AboutView(request):
    return render(request, 'about/about.html')


def AboutForm(request):
    if request.method == 'POST':
        form = AboutForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد')
        else:
            messages.warning(request, 'لطفا اطلاعات رو به درستی پر کنید')

    return redirect('home:home')
