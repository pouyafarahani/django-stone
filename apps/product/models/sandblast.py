from .base_models.base import BaseModel

from django.db import models


class SandblastModel(BaseModel):
    image = models.ImageField(upload_to='cover_sandblast/')
