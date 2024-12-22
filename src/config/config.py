from pydantic import BaseModel
from dotenv import dotenv_values

config = dotenv_values(".env")

# Load environment variables from the .env file
class DatabaseSettings(BaseModel):
    host:str = config['DATABASE_HOST']
    port:int = config['DATABASE_PORT']
    user:str = config['DATABASE_USER']
    password:str = config['DATABASE_USER_PASSWORD']
    database:str = config['DATABASE_NAME']
    ssl_mode:str = config['DATABASE_SSL_MODE']
    client_cert:str = config['DATABASE_CLIENT_CERT']
    ca_cert:str = config['DATABASE_CA_CERT']
    client_key:str = config['DATABASE_CLIENT_KEY']


class RapidAPISettings(BaseModel):
    url:str = config['RAPIDAPI_URL']
    key:str = config['RAPIDAPI_KEY']
    host:str = config['RAPIDAPI_HOST']

rapid_api = RapidAPISettings()
# Rapid API

