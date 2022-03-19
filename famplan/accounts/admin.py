from django.contrib import admin

# Register your models here.
from famplan.accounts.models import FamilyUser


@admin.register(FamilyUser)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name')
