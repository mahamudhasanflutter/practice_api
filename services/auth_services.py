from sqlalchemy.orm import Session

from models import User

from auth import (
    hash_password,
    verify_password,
    create_access_token
)

# =========================

# REGISTER USER

# =========================

def register_user(
    db: Session,
    user
):


    print("\n========== REGISTER SERVICE ==========")

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        return {
            "success": False,
            "message": "Email already exists"
        }

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    print("User Registered Successfully")

    return {
        "success": True,
        "message": "User Registered Successfully",
        "user_id": new_user.id
    }


# =========================

# LOGIN USER

# =========================

def login_user(
    db: Session,
    user
):


    print("\n========== LOGIN SERVICE ==========")

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:

        return {
            "success": False,
            "message": "Invalid Email"
        }

    if not verify_password(
        user.password,
        existing_user.password
    ):

        return {
            "success": False,
            "message": "Wrong Password"
        }

    token = create_access_token(
        {
            "user_id": existing_user.id,
            "email": existing_user.email
        }
    )

    print("Login Successful")

    return {
        "success": True,
        "message": "Login Successful",
        "access_token": token,
        "token_type": "bearer"
    }


# =========================

# UPDATE PROFILE

# =========================

def update_profile_service(
    db: Session,
    user_id: int,
    user
):


    print("\n========== UPDATE PROFILE ==========")

    existing_user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not existing_user:

        return {
            "success": False,
            "message": "User Not Found"
        }

    existing_user.name = user.name
    existing_user.email = user.email

    db.commit()

    print("Profile Updated")

    return {
        "success": True,
        "message": "Profile Updated Successfully"
    }

