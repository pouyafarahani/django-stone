from django.contrib import admin

from .models.tombstone import TombstoneModel

from .models.base_models.ForeignKey.specifications import SpecificationsModel


class SpecificationsModelInline(admin.TabularInline):
    model = SpecificationsModel
    extra = 1


@admin.register(TombstoneModel)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [SpecificationsModelInline]
