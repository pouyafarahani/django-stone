from .models.tombstone import TombstoneModel
from .models.sandblast import SandblastModel
from .models.wholesale import WholesaleModel
from .models.inscription import InscriptionModel
from .models.base_models.ForeignKey.specifications import SpecificationsModel

from django.contrib import admin


class SpecificationsInline(admin.TabularInline):
    model = SpecificationsModel
    extra = 1


@admin.register(TombstoneModel)
class TombstoneModelAdmin(admin.ModelAdmin):
    inlines = [SpecificationsInline]


@admin.register(InscriptionModel)
class InscriptionAdmin(admin.ModelAdmin):
    inlines = [SpecificationsInline]


@admin.register(SandblastModel)
class SandblastAdmin(admin.ModelAdmin):
    inlines = [SpecificationsInline]


@admin.register(WholesaleModel)
class WholesaleAdmin(admin.ModelAdmin):
    inlines = [SpecificationsInline]
