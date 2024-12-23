from fastapi import FastAPI
import uvicorn

# Import the Logger class from the previous implementation
from Logger.Logger import Logger
from utils.generalUtils import generate_request_id, ConnectToDB
from routes import user, funds, portfolio

from fastapi_cache import caches, close_caches
from fastapi_cache.backends.redis import CACHE_KEY, RedisCacheBackend

# Initialize the logger
logger = Logger(__name__)

# Create the FastAPI app
app = FastAPI()

@app.on_event("startup")
async def startup():
    ConnectToDB()

# add routers 
app.include_router(user.router)
app.include_router(funds.router)
app.include_router(portfolio.router)

@app.get("/")
async def read_root(logger=logger):
    unique_request_id = generate_request_id()
    logger.log("Received a request ", unique_request_id)
    return {"message": "FundHive v1.0.0"}

# Entry point for running the application
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, )
