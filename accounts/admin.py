from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from accounts.models import UserProfiles


class UserProfilesInline(admin.TabularInline):
    model = UserProfiles


class UserAdmin(DjangoUserAdmin):
    inlines = [
        UserProfilesInline,
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
