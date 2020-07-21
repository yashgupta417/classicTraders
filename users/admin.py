from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('user_id','username', 'password','name','mobile_number','role','active','staff','admin')}),
    )
    list_display = ('username', 'name','role')
    list_filter = ('role',)
    search_fields = ('username','name')
    ordering = ('username',)
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2','name','role','mobile_number')}
        ),
    )
    filter_horizontal = ()

admin.site.register(User,CustomUserAdmin)

from django.contrib.auth.models import Group
admin.site.unregister(Group)