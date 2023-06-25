from django.contrib import admin
from .models import Product,Order
# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Shopping site"
admin.site.index_title = "Manage shopping site"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_price','product_desc','discount_price','category')
    search_fields = ('product_name','category')
    list_editable = ('discount_price',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name','email','city','state','address','zip')
    search_fields = ('name','email')


admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)


