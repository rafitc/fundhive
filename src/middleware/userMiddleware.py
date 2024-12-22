from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from datetime import datetime

class JWTBearer(HTTPBearer):
    async def __call__(self, credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
        token = credentials.credentials
        try:
            # Decode and validate the token
            payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"]) # TODO move to config
            # Optionally, you can check for expiration manually
            if "exp" in payload and datetime.utcfromtimestamp(payload["exp"]) < datetime.now():
                raise HTTPException(status_code=401, detail="Token has expired")

            return payload['sub']  # Return the payload (user information) to the route

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

