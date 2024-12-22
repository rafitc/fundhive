from fastapi import APIRouter, Depends
import globalVars.global_vars as globalVars

from Database.DatabaseManager import Database
from utils.generalUtils import generate_request_id
from middleware.userMiddleware import JWTBearer
from services.fundsService import get_fund_house_data, get_fund_house_scheme, buy_fund_house_scheme
from model.fundModel import BuyFundPayload


router = APIRouter (
    prefix="/fund",
    tags=['fund'],
)

@router.get('/list-fund-houses')
def list_fund_house(request_id: str = Depends(generate_request_id), user: dict = Depends(JWTBearer())): #-- disabled jwt. will fix it later
    db:Database = globalVars.DB
    result = get_fund_house_data(db)
    return result


@router.get('/list-fund-schema')
def list_fund(fund_house_id:int = 0, request_id: str = Depends(generate_request_id), user: dict = Depends(JWTBearer())): #--user: dict = Depends(JWTBearer()) disabled jwt. will fix it later
    db:Database = globalVars.DB
    result = get_fund_house_scheme(db, fund_house_id)
    return result

@router.post('/buy-fund-schema', )
def buy_fund(payload:BuyFundPayload, request_id: str = Depends(generate_request_id), user: dict = Depends(JWTBearer())): #--user: dict = Depends(JWTBearer()) disabled jwt. will fix it later
    db:Database = globalVars.DB
    result = buy_fund_house_scheme(db, payload, user)
    return result