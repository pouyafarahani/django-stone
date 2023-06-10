# مدل کتیبه
from .base_models.base import BaseModel

from django.db import models


class InscriptionModel(BaseModel):
    image = models.ImageField(upload_to='cover_inscription/')
