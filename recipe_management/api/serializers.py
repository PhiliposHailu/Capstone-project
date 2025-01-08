from rest_framework import serializers
from django.contrib.auth import get_user_model
from recipe.models import Recipe, Ingredient, Category

User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")

class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"

class IngredientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"