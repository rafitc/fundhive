import uuid

from dotenv import dotenv_values
config = dotenv_values(".env")

from Database.DatabaseManager import Database
import globalVars.global_vars as globalVars

# Utility function to generate a unique request ID
def generate_request_id() -> str:
    return str(uuid.uuid4())

class ConnectToDB():
    db = Database(
            host=config['DATABASE_HOST'],
            port=config['DATABASE_PORT'],
            username=config['DATABASE_USER'],
            password=config['DATABASE_USER_PASSWORD'],
            dbname=config['DATABASE_NAME'],
            ssl_mode="",
            ssl_cert="",
            ssl_key="",
            ssl_root_cert="",
            min_size=1,
            max_size=10,
        )
    db.connect()
    globalVars.DB = db


