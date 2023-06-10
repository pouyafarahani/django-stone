# مدل سنگ قبر
from .base_models.base import BaseModel

from django.db import models


class TombstoneModel(BaseModel):
    image = models.ImageField(upload_to='cover_tombstone/')
