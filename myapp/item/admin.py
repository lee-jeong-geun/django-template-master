from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')


admin.site.register(Item, ItemAdmin)