from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "id", "email")

#adds my custom user to the admin page
admin.site.register(User, CustomUserAdmin)