from .views import AboutView, AboutForm

from django.urls import path

app_name = 'about'

urlpatterns = [
    path('', AboutView, name='about'),
    path('about-form/', AboutForm, name='form'),
]
