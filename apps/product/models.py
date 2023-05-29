from django.db import models


class ProductModel(models.Model):
    title = models.CharField(max_length=80)

    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True, null=True)
    percent = models.PositiveIntegerField(blank=True, null=True)

    image = models.ImageField(upload_to='cover_product/')

    def __str__(self):
        return self.title
