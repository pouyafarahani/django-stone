# مدل عمده فروشی
from .base_models.base import BaseModel

from django.db import models


class WholesaleModel(BaseModel):
    image = models.ImageField(upload_to='cover_wholesale/')
