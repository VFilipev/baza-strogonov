#! -*- encoding=UTF-8  -*-
from django.contrib import admin
from order import models

class PaymentInline(admin.TabularInline):
    model=models.Payment        
    extra=1
    can_delete = False

class OrderLodgeInline(admin.TabularInline):
    model=models.Order_lodge
    list_display = ('__all__',)
    extra=1
    can_delete = True

class ServiceInline(admin.TabularInline):
    model=models.Service
    list_display = ('__all__',)        
class ProductInline(admin.TabularInline):
    model=models.Product
    list_display = ('__all__',)    
# Register your models here.

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines=[
        PaymentInline,
        OrderLodgeInline,
        ServiceInline,
        ProductInline,
    ]
admin.site.register(models.Product)
admin.site.register(models.Uslugi)