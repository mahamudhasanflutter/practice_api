from fastapi import APIRouter, Header
from sqlalchemy.orm import Session

from database import SessionLocal

from schemas import (
    UserCreate,
    UserLogin,
    UserUpdate
)

from services.auth_services import (
    register_user,
    login_user,
    update_profile_service
)

from auth import verify_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# =========================
# REGISTER
# =========================

@router.post("/register")
def register(user: UserCreate):

    db: Session = SessionLocal()

    try:

        return register_user(
            db,
            user
        )

    finally:

        db.close()


# =========================
# LOGIN
# =========================

@router.post("/login")
def login(user: UserLogin):

    db: Session = SessionLocal()

    try:

        return login_user(
            db,
            user
        )

    finally:

        db.close()


# =========================
# PROFILE
# =========================

@router.get("/profile")
def profile(
    authorization: str = Header(...)
):

    token = authorization.replace(
        "Bearer ",
        ""
    )

    payload = verify_token(token)

    return {
        "success": True,
        "message": "Access Granted",
        "user": payload
    }


# =========================
# UPDATE PROFILE
# =========================

@router.put("/profile/update/{user_id}")
def update_profile(
    user_id: int,
    user: UserUpdate
):

    db: Session = SessionLocal()

    try:

        return update_profile_service(
            db,
            user_id,
            user
        )

    finally:

        db.close()