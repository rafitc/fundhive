from Database.DatabaseManager import Database
from fastapi import HTTPException
from model.fundModel import BuyFundPayload
from starlette.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_200_OK

from dotenv import dotenv_values
config = dotenv_values(".env")


class NoFundHouseFound(HTTPException):
    def __init__(self, detail: str = "No data found"):
        super().__init__(status_code=HTTP_204_NO_CONTENT, detail=detail)

class NoSchemeFound(HTTPException):
    def __init__(self, detail: str = "No Schema found for this fund house"):
        super().__init__(status_code=200, detail=detail)


def get_fund_house_data(db:Database):
    query = "select id, name from fund_families;"
    all_fund_houses = db.fetch(query)

    if not all_fund_houses:
        raise NoFundHouseFound
    
    return all_fund_houses

def get_fund_house_scheme(db:Database, fund_house_id):
    query = f"""select id, scheme_code, scheme_name, net_asset_value, 
            scheme_type, scheme_category from mutual_fund_schemes
            where fund_family_id = {fund_house_id} """
    print(query)
    fund_house_scheme = db.fetch(query)

    if not fund_house_scheme:
        raise NoSchemeFound
    
    return fund_house_scheme

def buy_fund_house_scheme(db:Database, payload:BuyFundPayload, user):
    query = f"""select id from portfolios
                where user_id = {user}; """
    portfolio_id = db.fetch(query)

    if not portfolio_id:
        # create a portfolio, 
        query = f"INSERT into portfolios (user_id) VALUES ({user}) RETURNING id;"
        portfolio_id = db.execute(query)

    # get mutual fund schema id 
    query = "SELECT id from mutual_fund_schemes where scheme_code = %s"
    portfolio = db.fetch(query, payload.scheme_code)
    schema_id = portfolio[0]['id']

    # assign to the user
    query = f"""INSERT into portfolio_mutual_funds (portfolio_id, mutual_fund_scheme_id, units, purchase_price) VALUES (
            {portfolio_id[0]['id']}, {schema_id},{ payload.units}, {payload.purchase_price});"""
    portfolio = db.execute(query)
    
    return {"message":"Mutual fund purchased successfully"}