from django.contrib import admin
from.models import Products
# Register your models here.
class TeamAdmin(admin.ModelAdmin):
        

        list_display = ('id', 'name', 'weight', 'price', 'created_at','updated_at')
        list_display_links = ('name', 'id')
        search_fields = ('name', 'weight')
        list_filter = ('price',)



admin.site.register(Products,TeamAdmin)