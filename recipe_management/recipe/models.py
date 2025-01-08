from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model() # proper way to retrive the user model

class Ingredient(models.Model):
    Ingredient_name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.Ingredient_name

class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):

    # CATAGORY = [
    #     ('Dessert', 'Dessert'),
    #     ('Main_Course', 'Main_Course'),
    # ]

    title =                         models.CharField(max_length=100, blank=False)
    description =                   models.TextField(max_length=300)
    publisher=                      models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipe_publisher')
    category =                      models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='recipe_category')
    ingredients =                   models.ManyToManyField(Ingredient, related_name='recipe_ingredients', blank=False)
    instructions =                  models.TextField(max_length=1000, blank=False)
    preparation_time =              models.PositiveIntegerField(help_text="preparation time in minutes eg. 30 or 90")
    cooking_time =                  models.PositiveIntegerField(help_text="cooking time in minutes")
    servings=                       models.PositiveIntegerField(null=True, blank=True)
    created_date=                   models.DateTimeField(auto_now_add=True)
    updated_date=                   models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title