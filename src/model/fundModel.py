from pydantic import BaseModel

class BuyFundPayload(BaseModel):
    scheme_code: int
    units: float
    purchase_price: float


