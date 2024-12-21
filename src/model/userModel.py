from pydantic import BaseModel


class SignupPayload(BaseModel):
    name: str
    email: str
    password: str


class SigninPayload(BaseModel):
    email: str
    password: str


