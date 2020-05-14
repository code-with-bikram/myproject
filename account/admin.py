from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import Group


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']

admin.site.unregister(Group)
