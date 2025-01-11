
## **A. Authentication**

### **1. Authenticate a User**
**Method:** `POST`
**Endpoint:** `/api/token/`

**Description:** user can get access tokens.

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

**Sample Response: returns tokens**
```json
{
    "token" : "eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV"

}

```
<!-- this token can be used to get full access to our api views that require user login/authentication -->

## **Instructions to implement user Authentication**

open postman/browser
set method to post(in postman)
use this url "http://127.0.0.1:8000/api/token/"
go to body, raw and json to get the token by enring the sample request above in to the body
after that copy the access token and go to authorization tab and select type "Bearer token" after that paste your access token in to the token box and you are now authticated and can do everthing that an authenticated user can do.