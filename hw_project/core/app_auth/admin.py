from django.contrib import admin

from core.app_auth.models import User, Profile

# Register your models here.
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
    
    
