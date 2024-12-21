from Database.DatabaseManager import Database
from model.userModel import SignupPayload, SigninPayload
from datetime import datetime, timedelta


import bcrypt, jwt
from psycopg2.errors import UniqueViolation

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

class UserAlreadyExistsException(HTTPException):
    def __init__(self, detail: str = "User with this email already exists"):
        # Set the status code to 400 Bad Request
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)


class InvalidCredentialsException(HTTPException):
    def __init__(self, detail: str = "Invalid email or password"):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)


def signupService(db: Database, payload: SignupPayload):
    # Step 1: Check if user already exists with the provided email
    query = "SELECT id FROM public.users WHERE email = %s"
    existing_user = db.fetch(query, payload.email)

    if existing_user:
        # Raise the custom exception if user already exists
        raise UserAlreadyExistsException()

    # Step 2: Hash the password
    password_hash = bcrypt.hashpw(payload.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Step 3: Insert the new user into the database
    insert_query = """
        INSERT INTO public.users (email, password_hash, created_at, updated_at)
        VALUES (%s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
    """
    try:
        db.execute(insert_query, payload.email, password_hash)
    except UniqueViolation:
        # In case of a race condition or other issues, raise the custom exception
        raise UserAlreadyExistsException()
    
    # Return a success message or any other response as needed
    return {"message": "User successfully created."}

def signinService(db: Database, payload: SigninPayload):
    # Step 1: Check if the user exists with the provided email
    query = "SELECT id, password_hash FROM public.users WHERE email = %s"
    user = db.fetch(query, payload.email)
    
    if not user:
        raise InvalidCredentialsException()

    # Step 2: Check if the password matches the hash
    stored_password_hash = user[0]["password_hash"]
    if not bcrypt.checkpw(payload.password.encode('utf-8'), stored_password_hash.encode('utf-8')):
        raise InvalidCredentialsException()

    # Step 3: Generate an authentication token (JWT)
    # Set the expiration time for 1 day
    expiration_time = datetime.utcnow() + timedelta(days=1) # TODO move to config file

    token_data = {
        "sub": user[0]['id'],  # The subject of the token, typically the user identifier
        "exp": expiration_time  # Expiry time
    }
    token = jwt.encode(token_data, "SECRET_KEY", algorithm="HS256") #TODO move the secret key to read from .env

    # Step 4: Return the token
    return {"access_token": token, "token_type": "bearer"}
