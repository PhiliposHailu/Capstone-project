# Generated by Django 5.1.4 on 2025-01-07 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ingredient_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('instructions', models.TextField(max_length=1000)),
                ('preparation_time', models.IntegerField(help_text='preparation time in minutes eg. 30 or 90')),
                ('cooking_time', models.IntegerField(help_text='cooking time in minutes')),
                ('servings', models.IntegerField(help_text='number of people you can feed')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipe_category', to='recipe.category')),
                ('ingredients', models.ManyToManyField(related_name='recipe_ingredients', to='recipe.ingredient')),
            ],
        ),
    ]
