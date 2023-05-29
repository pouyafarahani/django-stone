from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # panel admin
    path('admin/', admin.site.urls),

    # local apps
    path('', include('home.urls')),
]
