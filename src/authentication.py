"""_summary_
"""
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from dotenv import load_dotenv
import jwt
import os

load_dotenv(dotenv_path='.env')
SECRET_KEY = os.getenv("SECRET_KEY")

security = HTTPBearer()

def generate_jwt():
    return jwt.encode({"role": "user"}, SECRET_KEY, algorithm="HS256")

def decode_jwt(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
def authenticate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    decode_jwt(credentials.credentials)
