from django.contrib import admin
from .models import Category, Recipe, Ingredient


class CustomRecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher')
    
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe, CustomRecipeAdmin)