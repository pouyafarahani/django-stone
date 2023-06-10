from django.db import models

from apps.product.models.base_models.base import BaseModel


class SpecificationsModel(models.Model):
    product = models.ForeignKey(BaseModel, on_delete=models.CASCADE, related_name='specifications')
    title = models.CharField(max_length=80)
