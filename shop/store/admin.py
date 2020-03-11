from django.contrib import admin
from .models import Product, Basket

class ProductAdmin(admin.ModelAdmin):
    list_display = ('image_img', 'header_link', 'vendor_code', 'price_format', 'create_date', 'settings')


admin.site.register(Product, ProductAdmin)
admin.site.register(Basket)
