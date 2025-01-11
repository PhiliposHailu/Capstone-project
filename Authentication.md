# Authentication Guide for Recipe Management API

A document that provides an overview of the authentication system implemented in the recipe management api. The API uses JSON Web Token(JWT) authentication to secure its endpoints.

---

## Overview of Authentication
The API uses the `djangorestframework-simplejwt` library for JWT-based authentication. There are two types of tokens that are generated:
- **Access Token**: Used for authenticating API requests.
- **Refresh Token**: Used to obtain a new access token after the current one expires.

### Endpoints for Token Management

#### Token Obtain
- **URL**: `/api/token/`
- **Method**: `POST`
- **Description**: Generates an access token and a refresh token for the user.
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
- **Description**: used to generate a new access token with the refresh token.
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

## Protecting API Endpoints

Protected endpoints require the user to include the `Authorization` header in their requests, using the format:

```
Authorization: Bearer <access_token>
```

For example:
- **Key**: `Authorization`
- **Value**: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`

If a valid token is not provided, the API will respond with:
```json
{
    "detail": "Authentication credentials were not provided."
}
```

---

## Configuring JWT in Django
The following configurations are added to `settings.py` to enable JWT authentication:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}
```

---

## Example Workflow
### Step 1: Register a User
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
- **Response**: A list of recipes if the token is valid.

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

<!-- ---

## Common Errors and Resolutions

### Error: "Token is invalid or expired."
- **Cause**: The access token is no longer valid.
- **Solution**: Use the refresh token to obtain a new access token.

### Error: "Authentication credentials were not provided."
- **Cause**: The `Authorization` header is missing or incorrectly formatted.
- **Solution**: Ensure the header is present and uses the format: `Bearer <access_token>`.

### Error: "Invalid refresh token."
- **Cause**: The provided refresh token is invalid or has expired.
- **Solution**: Log in again to obtain a new pair of tokens.

--- -->
