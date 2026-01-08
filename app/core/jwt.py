import os
from datetime import datetime, timedelta
from jose import jwt

ALGORITHM = "HS256"
SECRET_KEY = os.getenv("JWT_SECRET")  # read at runtime

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update({"exp": expire})
    
    print("DEBUG TO_ENCODE:", to_encode)
    print("DEBUG SECRET_KEY TYPE:", type(SECRET_KEY))
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
