from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
