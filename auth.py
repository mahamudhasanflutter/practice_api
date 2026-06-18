import bcrypt

from jose import jwt
from datetime import datetime, timedelta

from config import (
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from config import ENABLE_AUTH

def check_auth(token: str = None):

    if not ENABLE_AUTH:
        print("Auth Disabled")
        return {
            "user_id": 0,
            "email": "test@test.com"
        }

    if not token:
        raise Exception("Token Required")

    return verify_token(token)

print("Auth Module Loaded")


def hash_password(password: str):

    print("Hashing Password...")

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(
        password.encode(),
        salt
    )

    return hashed_password.decode()


def verify_password(
    plain_password: str,
    hashed_password: str
):

    print("Verifying Password...")

    return bcrypt.checkpw(
        plain_password.encode(),
        hashed_password.encode()
    )


def create_access_token(data: dict):

    print("Creating JWT Token...")

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    print("Token Created")

    return token


def verify_token(token: str):

    print("Verifying Token...")

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload

def get_current_user(token: str):

    payload = verify_token(token)

    return payload