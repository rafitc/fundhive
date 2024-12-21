from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv("config/.env")

class Settings(BaseModel):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"  # Ensure .env file is loaded
        env_file_encoding = 'utf-8'  # Optional: to specify encoding of the .env file

# Create an instance of Settings to access the environment variables
settings = Settings()

# Accessing settings
print(settings.database_url)  # Example usage of the settings object
print(settings.secret_key)
