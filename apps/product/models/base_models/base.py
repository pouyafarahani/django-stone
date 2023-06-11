from django.db import models

from ckeditor.fields import RichTextField


class BaseModel(models.Model):
    name = models.CharField(max_length=80, blank=True)

    price = models.PositiveIntegerField(blank=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    percent = models.PositiveIntegerField(blank=True, null=True)

    short_description = RichTextField(blank=True)
    description = RichTextField(blank=True)

