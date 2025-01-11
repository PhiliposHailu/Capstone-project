#Django Capstone Project: Recipe Managemetn API: Endpoints Documentation

## **Endpoints with Examples**

## **A. User Authentication**

### **1. Authenticate a User**
**Method:** `POST`
**Endpoint:** `/api/token/`

**Description:** user can get tokens.

**Request Parameters:**
- `username` (string, required): The username for the user.
- `password` (string, required): The password for the user.

**Sample Request:**
```json
{
  "username": "john_doe",
  "password": "password123",
}
```

**Sample Response:**
```json
{
    "token": "alkghaoa2q9587",
}

```

### **2. Register a New User**
**Method:** `POST`
**Endpoint:** `/api/register/`

**Description:** new user can register.

**Request Parameters:**
- `username` (string, required): The username for the user.
- `password` (string, required): The password for the user.
- `email` (string, optional): Email address of the user.

**Sample Request:**
```json
{
    "username": "mike",
    "email": "mike@gmail.com",
    "password": "temp",
}
```

**Sample Response:**
```json
{
    "id": 1,
    "username": "mike",
    "email": "mike@gmail.com",
}

```
---

## **Recipe Management**

### **1. Create a New Recipe**

**Method:** `POST`
**Endpoint:** `/api/create/`

**Description:** authenticated users can create a new recipe.

**Request Parameters:**
- `title` (string, required): The name of the recipe.
- `ingredients` (array of strings, required): A list of ingredients.
- `instructions` (string, required): The steps to prepare the recipe.
- `categories` (array of strings, optional): Categories associated with the recipe.

**Sample Request:**
```json
{
  "title": "doro wot",
  "ingredients": ["chicken", "eggs", "parmesan cheese", "bacon"],
  "instructions": "Boil chicken. Cook bacon. Mix eggs and cheese. Combine everything.",
  "categories": ["Ethiopian", "Dinner"]
}
```

**Sample Response:**
```json
{
    "id": 1,
    "title": "doro wot",
    "ingredients": ["chicken", "eggs", "parmesan cheese", "bacon"],
    "instructions": "Boil chicken. Cook bacon. Mix eggs and cheese. Combine everything.",
    "categories": ["Ethiopian", "Dinner"],
    "message": "Recipe created successfully",

}
```

---

### **2. Retrieve All Recipes**
**Method:** `GET`
**Endpoint:** `/api/list/`

**Description:** lists all available recipes.

**Request Parameters:** 

**Sample Response:**
```json
[
  {
    "id": 1,
    "title": "doro wot",
    "ingridients": "chiken meat, eggs, onions, oil, butter",
    "categories": ["Ethiopian", "Dinner"]
  },
  {
    "id": 2,
    "title": "Chicken Curry",
    "ingridients": "meat, eggs, onions, oil, butter",
    "categories": ["Indian", "Dinner"]
  }
]
```

---

### **3. Retrieve a Recipe by ID**
**Method:** `GET`
**Endpoint:** `/api/list/<id>/`

**Description:** details of a specific recipe by its ID.

**Path Parameter:**
- `<id>` (integer, required): The ID of the recipe.

**Sample Response:**
```json
{
  "id": 1,
  "title": "dorow wot
  ",
  "ingredients": ["dorow", "eggs", "parmesan cheese", "bacon"],
  "instructions": "Boil chicken. Cook bacon. Mix eggs and cheese. Combine everything.",
  "categories": ["Ethiopian", "Dinner"]
}
```

---

### **4. Update a Recipe by ID**
**Method:** `PUT`
**Endpoint:** `/api/update/<id>/`

**Description:** Updates an existing recipe by its ID.

**Path Parameter:**
- `<id>` (integer, required): The ID of the recipe.

**Request Parameters:**
- `title` (string, optional): Updated title for the recipe.
- `ingredients` (array of strings, optional): Updated list of ingredients.
- `instructions` (string, optional): Updated instructions.
- `categories` (array of strings, optional): Updated categories.

**Sample Request:**
```json
{
  "title": "dorow wot
   Deluxe",
  "ingredients": ["dorow", "eggs", "parmesan cheese", "bacon", "cream"],
  "instructions": "Boil chicken. Cook bacon. Mix eggs, cheese, and cream. Combine everything.",
  "categories": ["Ethiopian", "Dinner"]
}
```

**Sample Response:**
```json
{
    "id": 1,
    "title": "dorow wot
     Deluxe",
    "ingredients": ["dorow", "eggs", "parmesan cheese", "bacon", "cream"],
    "instructions": "Boil chicken. Cook bacon. Mix eggs, cheese, and cream. Combine everything.",
    "categories": ["Ethiopian", "Dinner"],
    
}
```

---

### **5. Delete a Recipe by ID**
**Method:** `DELETE`
**Endpoint:** `api/delete/<id>/`


**Description:** Deletes a specific recipe by its ID.

**Path Parameter:**
- `<id>` (integer, required): The ID of the recipe.

**Sample Response:**
```json
{
  // recipe with that id is deleted
}
```

---

## **Filtered Viewing Endpoints**

### **1. Retrieve Recipes by publisher**
**Method:** `GET`
**Endpoint:** `api/filter/<id>/`

**Description:** Retrieves recipes filtered by a specific publishers id.

**Path Parameter:**
- `<id>` (integer, required): The ID of the any publisher id.


**Sample Response:**
```json
[
  {
    "user_id": 1,
    "title": "dorow wot",
    "categories": ["Ethiopian", "Dinner"]
  }

  {
    "user_id": 1,
    "title": "fried eggs",
    "categories": ["breakfast"]
  }
]
```

---
