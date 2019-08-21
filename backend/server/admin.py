from django.contrib import admin

from .models import ShoppingMall, Category, Item

# Register your models here.
admin.site.register(ShoppingMall)
admin.site.register(Category)
admin.site.register(Item)