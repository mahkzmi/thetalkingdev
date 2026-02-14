from django.contrib import admin
from .models import ServicePackage

@admin.register(ServicePackage)
class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_crypto', 'delivery_days')
