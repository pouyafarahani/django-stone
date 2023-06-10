from django.urls import path

from .view.tombstone_view import TombstoneListView, TombstoneDetailView

app_name = 'product'

urlpatterns = [
    path('list/', TombstoneListView.as_view(), name='product_list'),
    path('detail/<int:pk>/', TombstoneDetailView.as_view(), name='product_detail'),
]
