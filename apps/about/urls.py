from django.urls import path

from .views import AboutView, AboutForm

app_name = 'about'

urlpatterns = [
    path('', AboutView, name='about'),
    path('about-form/', AboutForm, name='form'),
]
