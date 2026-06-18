from fastapi import APIRouter, Header
from sqlalchemy.orm import Session

from database import SessionLocal

from schemas import (
    ProductCreate,
    ProductUpdate
)

from auth import check_auth

from services.product_services import (
    create_product_service,
    get_products_service,
    get_product_service,
    update_product_service,
    delete_product_service,
    search_product_service,
    pagination_service
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

# =========================

# CREATE PRODUCT

# =========================

@router.post("/")
def create_product(
    product: ProductCreate,
    authorization: str = Header(None)
):


    check_auth(authorization)

    db: Session = SessionLocal()

    try:

        return create_product_service(
            db,
            product
        )

    finally:

        db.close()


# =========================

# GET ALL PRODUCTS

# =========================

@router.get("/")
def get_products():

    
    db: Session = SessionLocal()

    try:

        return get_products_service(
            db
        )

    finally:

        db.close()
    

# =========================

# GET SINGLE PRODUCT

# =========================

@router.get("/{product_id}")
def get_product(
    product_id: int
):


    db: Session = SessionLocal()

    try:

        return get_product_service(
            db,
            product_id
        )

    finally:

        db.close()

# =========================

# UPDATE PRODUCT

# =========================

@router.put("/{product_id}")
def update_product(
    product_id: int,
    product: ProductUpdate,
    authorization: str = Header(None)
):


    check_auth(authorization)

    db: Session = SessionLocal()

    try:

        return update_product_service(
            db,
            product_id,
            product
        )

    finally:

        db.close()


# =========================

# DELETE PRODUCT

# =========================

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    authorization: str = Header(None)
):


    check_auth(authorization)

    db: Session = SessionLocal()

    try:

        return delete_product_service(
            db,
            product_id
        )

    finally:

        db.close()


# =========================

# SEARCH PRODUCT

# =========================

@router.get("/search/{keyword}")
def search_product(
    keyword: str
):


    db: Session = SessionLocal()

    try:

        return search_product_service(
            db,
            keyword
        )

    finally:

        db.close()


# =========================

# PAGINATION

# =========================

@router.get("/page/list")
def pagination(
    page: int = 1,
    limit: int = 5
):


    db: Session = SessionLocal()

    try:

        return pagination_service(
            db,
            page,
            limit
        )

    finally:

        db.close()

