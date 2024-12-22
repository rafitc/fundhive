import uuid

from dotenv import dotenv_values
config = dotenv_values(".env")

from Database.DatabaseManager import Database
import globalVars.global_vars as globalVars
from config.config import DatabaseSettings

# Utility function to generate a unique request ID
def generate_request_id() -> str:
    return str(uuid.uuid4())

class ConnectToDB():
    connection = DatabaseSettings()
    db = Database(
            host=connection.host,
            port=connection.port,
            username=connection.user,
            password=connection.password,
            dbname=connection.database,
            ssl_mode="",
            ssl_cert="",
            ssl_key="",
            ssl_root_cert="",
            min_size=1,
            max_size=10,
        )
    db.connect()
    globalVars.DB = db


