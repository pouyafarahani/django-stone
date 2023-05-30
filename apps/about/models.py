from django.db import models


class AboutModel(models.Model):
    full_name = models.CharField(max_length=60)
    body = models.CharField(max_length=600)

    def __str__(self):
        return self.full_name
