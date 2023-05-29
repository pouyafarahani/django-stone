from django.urls import path

from .views import AboutView

app_name = 'about'

urlpatterns = [
    path('', AboutView, name='about'),
]
