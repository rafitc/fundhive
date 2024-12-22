from fastapi import APIRouter, Depends
import globalVars.global_vars as globalVars

from Database.DatabaseManager import Database
from utils.generalUtils import generate_request_id
from middleware.userMiddleware import JWTBearer
from services.portfolio import fetch_portfolio


router = APIRouter (
    prefix="/portfolio",
    tags=['fund'],
)

@router.get('/view')
def view_portfolio(request_id: str = Depends(generate_request_id), user: dict = Depends(JWTBearer())): #-- disabled jwt. will fix it later
    db:Database = globalVars.DB
    result = fetch_portfolio(db, user)
    
    return result