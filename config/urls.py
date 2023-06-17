from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
                  # panel admin
                  path('armin/', admin.site.urls),

                  # local apps
                  path('', include('apps.home.urls')),
                  path('about/', include('apps.about.urls')),
                  path('product/', include('apps.product.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
