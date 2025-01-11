# Guide to Authentication for Recipe Management API

This document outlines the authentication framework used in the Recipe Management API, which relies on JSON Web Token (JWT) authentication to safeguard its endpoints.

---

## Overview of Authentication
The API leverages the `djangorestframework-simplejwt` library for implementing JWT-based authentication. Two types of tokens are generated:
- **Access Token**: Grants access to API endpoints.
- **Refresh Token**: Enables the generation of a new access token when the current one expires.

### Endpoints for Token Management

#### Token Obtain
- **URL**: `/api/token/`
- **Method**: `POST`
- **Description**: Issues an access token and refresh token for the user.
- **Request Body**:
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
      "refresh": "your_refresh_token",
      "access": "your_access_token"
  }
  ```

#### Token Refresh
- **URL**: `/api/token/refresh/`
- **Method**: `POST`
- **Description**:  Generates a new access token using the refresh token.
- **Request Body**:
  ```json
  {
      "refresh": "your_refresh_token"
  }
  ```
- **Response**:
  ```json
  {
      "access": "new_access_token"
  }
  ```

---

## Securing API Endpoints

Endpoints requiring authentication must include the `Authorization` header in the following format:

```
Authorization: Bearer <access_token>
```

For example:
- **Key**: `Authorization`
- **Value**: `Bearer pyJhbfciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`

If a valid token is not provided, the API will respond with:
```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

## JWT Configuration in Django
The following configurations are added to `settings.py` to enable JWT authentication:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=10),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=21),
}
```

---

## Authentication Workflow
### Step 1: Register a New User
- **URL**: `/api/register/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "new_user",
      "password": "secure_password",
      "email": "user@example.com"
  }
  ```

### Step 2: Obtain Tokens
- **URL**: `/api/token/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "username": "new_user",
      "password": "secure_password"
  }
  ```
- **Response**:
  ```json
  {
      "refresh": "your_refresh_token",
      "access": "your_access_token"
  }
  ```

### Step 3: Access a Protected Endpoint
- **Example**: Retrieve all recipes
- **URL**: `/api/retrieve/`
- **Method**: `GET`
- **Headers**:
  ```
  Authorization: Bearer <access_token>
  ```
- **Response**:Returns a list of recipes if the token is valid.

### Step 4: Refresh the Access Token
- **URL**: `/api/token/refresh/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
      "refresh": "your_refresh_token"
  }
  ```
- **Response**:
  ```json
  {
      "access": "new_access_token"
  }
  ```

