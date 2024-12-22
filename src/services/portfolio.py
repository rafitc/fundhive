
from Database.DatabaseManager import Database
from fastapi import HTTPException
from model.fundModel import BuyFundPayload
from starlette.status import HTTP_400_BAD_REQUEST

from dotenv import dotenv_values
config = dotenv_values(".env")

class UserNotFound(HTTPException):
    def __init__(self, detail: str = "User is not active"):
        # Set the status code to 400 Bad Request
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)


def fetch_portfolio(db:Database, user_id):
    # check whether the user exist or not 
    query = "select * from users where id = %s"
    user = db.fetch(query, (user_id))

    
    if not user:
        raise UserNotFound
    
    # then fetch all portfolio with value
    query  = """select ff."name", mfs.scheme_code, mfs.scheme_name, 
                mfs.scheme_type, mfs.scheme_category from portfolios p 
                join portfolio_mutual_funds pmf 
                on pmf.portfolio_id = p.id 
                join mutual_fund_schemes mfs 
                on mfs.id = pmf.mutual_fund_scheme_id 
                join fund_families ff 
                on ff.id = mfs.fund_family_id 
                where p.user_id = %s;"""
    portfolio = db.fetch(query, user_id)
    # calculate the current value 

    # compare it with current price and send the result back
    finalResult = []
    for each in portfolio: 
        result = {
            "fund-house-name":f"{each['name']}",
            "scheme-code": f"{each['scheme_code']}",
            "scheme-name": f"{each['scheme_name']}",
            "scheme-type": f"{each['scheme_type']}",
            "scheme-category": f"{each['scheme_category']}",
        }
        finalResult.append(result)
    return finalResult