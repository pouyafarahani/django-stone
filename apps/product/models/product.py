from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField


class ProductModel(models.Model):
    name = models.CharField(max_length=80, blank=True)

    price = models.PositiveIntegerField(blank=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    percent = models.PositiveIntegerField(blank=True, null=True)

    image = models.ImageField(upload_to='cover_product/')

    short_description = RichTextField(blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.pk])
