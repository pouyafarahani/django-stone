from django.urls import path

from .view import home_view

app_name = 'home'

urlpatterns = [
    path('', home_view, name='home'),
]
