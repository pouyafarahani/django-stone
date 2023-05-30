from django.db import models

from .product import ProductModel


class SpecificationsModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='specifications')
    title = models.CharField(max_length=80)
