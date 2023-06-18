from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .forms import AboutForms


def AboutView(request):
    return render(request, 'about/about.html')


@require_http_methods(["POST"])
def AboutForm(request):
    form = AboutForms(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'نظر شما با موفقیت ثبت شد')
    else:
        messages.warning(request, 'لطفا اطلاعات رو به درستی پر کنید')

    return redirect('home:home')
