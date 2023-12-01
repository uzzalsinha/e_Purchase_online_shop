from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import My_Account

# Register your models here.

class Account_Admin(UserAdmin):
    list_display = ('email', 'f_name', 'l_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email',)
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(My_Account, Account_Admin)