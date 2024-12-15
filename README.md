My Django Capstone Project

"""Detailed Endpoint and Examples"""

1, Get All Recipes

    method: GET
    endpoint: /api/recipes/

Response (Success):

[
  {
    "id": 1,
    "title": "Spaghetti Bolognese",
    "category": "Italian",
    "ingredients": ["spaghetti", "ground beef", "tomato sauce"],
    "user": 1
  },
  {
    "id": 2,
    "title": "Chicken Curry",
    "category": "Indian",
    "ingredients": ["chicken", "curry powder", "coconut milk"],
    "user": 2
  }
]



2, Create a Recipe

    method: POST
    endpoint: /api/recipes/create/

Request Body:

{
  "title": "Pancakes",
  "category": 3,
  "ingredients": ["flour", "milk", "eggs", "sugar"],
  "instructions": "Mix ingredients and cook on a hot pan."
}

Response (Success):

{
  "id": 3,
  "title": "Pancakes",
  "category": "Breakfast",
  "ingredients": ["flour", "milk", "eggs", "sugar"],
  "instructions": "Mix ingredients and cook on a hot pan.",
  "user": 1
}


3, Update a Recipe

    path: /api/recipes/<int:id>/update/
    method: PUT

    Description: update a recipe from the database by its ID.

Request Body:

{
  "title": "Vegan Pancakes",
  "category": "Breakfast",
  "ingredients": "Flour, Almond Milk, Maple Syrup",
  "instructions": "Mix all ingredients and warm on a pan."
}

Response(success):

{
  "id": 1,
  "title": "Vegan Pancakes",
  "category": "Breakfast",
  "ingredients": "Flour, Almond Milk, Maple Syrup",
  "instructions": "Mix all ingredients and warm on a pan."
}


4, Delete a Recipe

    path: /api/recipes/<int:id>/delete/
    method: DELETE

    Description: Delete a recipe from the database by its ID.

    Response (204 No Content):

        No content returned upon successful deletion.