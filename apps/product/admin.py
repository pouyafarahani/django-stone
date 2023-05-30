from django.contrib import admin

from .models.product import ProductModel

from .models.product_specifications import SpecificationsModel


class SpecificationsModelInline(admin.TabularInline):
    model = SpecificationsModel
    extra = 1


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [SpecificationsModelInline]
