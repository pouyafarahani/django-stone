from django.db import models

from ckeditor.fields import RichTextField
from django.urls import reverse


class TombstoneModel(models.Model):
    STATUS_CHOICES = (
        ('tombstone', 'سنگ قبر'),
        ('inscription', 'کتیبه'),
        ('sandblast', 'سندبلاست'),
        ('wholesale', 'عمده فروشی'),
    )

    name = models.CharField(max_length=255)
    group = models.CharField(choices=STATUS_CHOICES, max_length=50)

    image = models.ImageField(upload_to='cover_tombstone/')
    price = models.PositiveIntegerField(blank=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    percent = models.PositiveIntegerField(blank=True, null=True)

    short_description = RichTextField(blank=True)
    description = RichTextField(blank=True)

    def __str__(self):
        return f'{self.name} ==> {self.group}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.pk])
