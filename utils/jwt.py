import os 
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-dev-key-change-in-prod')
ALGORITHM = os.getenv('ALGORITHM','HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES', '30'))

def create_access_token(data: dict) -> dict:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

def verify_access_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        return None 
    