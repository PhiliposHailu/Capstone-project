from rest_framework import serializers
from django.contrib.auth import get_user_model
from recipe.models import Recipe, Ingredient, Category

User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

        #prevent our password from being read back to us in our API responses
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'] # here the password is hashed before it is saved
        )
            
        return user

class IngredientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "ingredients"

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class RecipeSerializers(serializers.ModelSerializer):
    # using __str__() representation of our ingrident model
    # ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = "id", "title", "ingredients", "instructions", "category"