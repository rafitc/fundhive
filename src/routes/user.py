from fastapi import APIRouter, Depends
import globalVars.global_vars as globalVars

from Database.DatabaseManager import Database
from utils.generalUtils import generate_request_id
from model.userModel import SignupPayload, SigninPayload
from services.authService import signupService, signinService



router = APIRouter (
    prefix="/user",
    tags=['user'],
)

@router.post('/signup')
def signup(payload:SignupPayload, request_id: str = Depends(generate_request_id)):
    db:Database = globalVars.DB
    
    result = signupService(db, payload)
    return result

@router.post('/signin')
def signup(payload:SigninPayload, request_id: str = Depends(generate_request_id)):
    db:Database = globalVars.DB
    
    result = signinService(db, payload)
    return result