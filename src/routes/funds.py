from fastapi import APIRouter, Depends
import globalVars.global_vars as globalVars

from Database.DatabaseManager import Database
from utils.generalUtils import generate_request_id
from middleware.userMiddleware import JWTBearer
from services.fundsService import get_master_data


router = APIRouter (
    prefix="/fund",
    tags=['fund'],
)

@router.get('/list-funds')
def signup(request_id: str = Depends(generate_request_id), ): #--user: dict = Depends(JWTBearer()) disabled jwt. will fix it later
    db:Database = globalVars.DB
    result = get_master_data()
    return result