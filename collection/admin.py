from django.contrib import admin
from . import models

class Collection_Admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('collection_name',)}
    list_display = ('collection_name', 'slug')

admin.site.register(models.Collection, Collection_Admin)