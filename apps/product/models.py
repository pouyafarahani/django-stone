from django.db import models
from django.urls import reverse


class ProductModel(models.Model):
    title = models.CharField(max_length=80)

    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    percent = models.PositiveIntegerField(blank=True, null=True)

    image = models.ImageField(upload_to='cover_product/')

    shor_description =

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.pk])
