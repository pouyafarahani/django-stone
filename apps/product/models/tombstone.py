from .base_models.base import BaseModel

from django.db import models
from django.urls import reverse


class TombstoneModel(BaseModel):
    image = models.ImageField(upload_to='cover_tombstone/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.pk])
