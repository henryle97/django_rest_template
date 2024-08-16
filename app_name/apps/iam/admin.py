from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

# Register your models here.

# By default, admin site already has User and Group models registered.
# If you want to customize the admin site, you can unregister the default models and register your own.
# admin.site.unregister(Group)
# admin.site.unregister(User)
# admin.site.register(User, CustomUserAdmin)
# admin.site.register(Group, CustomGroupAdmin)
