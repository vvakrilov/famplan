from django.contrib import admin

from famplan.accounts.models import UserProfile


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
