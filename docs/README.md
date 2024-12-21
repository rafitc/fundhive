# API Doc

## Endpoints

### 1. Get All Users

- **Endpoint:** `/signup`
- **Method:** `POST`
- **Description:** Create a account for the user
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "SomePassword"
  }
  ```
- **Response:**
  - **200 OK**
    ```json
    {
      "message": "User account created successfully"
    }
    ```
  - **401 BAD REQUEST**
    ```json
    {
      "message": "User email already exist"
    }
    ```
