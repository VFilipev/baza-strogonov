from django.contrib import admin
from lodge import models

class PriceInline(admin.TabularInline):
    model=models.Price


class SpecialPriceInline(admin.TabularInline):
    model=models.Special_price


class PhotosInline(admin.TabularInline):
    model=models.Photos
    extra = 10
class AvailabilityInline(admin.TabularInline):
    model=models.Availability

@admin.register(models.Lodge)
class OrderAdmin(admin.ModelAdmin):
    inlines=[
            PriceInline,
            SpecialPriceInline,
            PhotosInline,
            AvailabilityInline
             ]

class UslugiInline(admin.TabularInline):
    model=models.Uslugi

@admin.register(models.UslugiGroup)
class UslugiGroupAdmin(admin.ModelAdmin):
    inlines=[
            UslugiInline,
             ]

@admin.register(models.Photogroup)
class PhotoGroupAdmin(admin.ModelAdmin):
    inlines=[
            PhotosInline,
            ]

@admin.register(models.Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('id','lodge','name', 'days','cost')
    list_editable = ('name','lodge', 'days','cost')

# admin.site.register(OrderAdmin)
# admin.site.register(models.Photogroup,PhotoGroupAdmin)
# admin.site.register(models.UslugiGroup, UslugiGroupAdmin)
# admin.site.register(models.Price,PriceAdmin)
# admin.site.register(models.Photos)
# admin.site.register(models.Special_price)

