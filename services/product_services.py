from models import Product

# =========================

# CREATE PRODUCT

# =========================

def create_product_service(
    db,
    product
):


    print("\n========== CREATE PRODUCT ==========")

    new_product = Product(
        title=product.title,
        description=product.description,
        price=product.price,
        stock=product.stock
    )

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return {
        "success": True,
        "message": "Product Created Successfully",
        "product_id": new_product.id
    }


# =========================

# GET ALL PRODUCTS

# =========================

def get_products_service(
db
):


    print("\n========== GET PRODUCTS ==========")

    products = db.query(Product).all()

    return products


    # =========================

    # GET SINGLE PRODUCT

    # =========================

def get_product_service(
    db,
    product_id: int
):


    print("\n========== GET PRODUCT ==========")

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:

        return {
            "success": False,
            "message": "Product Not Found"
        }

    return product


    # =========================

    # UPDATE PRODUCT

    # =========================

def update_product_service(
    db,
    product_id: int,
    product
):


    print("\n========== UPDATE PRODUCT ==========")

    existing_product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not existing_product:

        return {
            "success": False,
            "message": "Product Not Found"
        }

    existing_product.title = product.title
    existing_product.description = product.description
    existing_product.price = product.price
    existing_product.stock = product.stock

    db.commit()

    return {
        "success": True,
        "message": "Product Updated Successfully"
    }


# =========================

# DELETE PRODUCT

# =========================

def delete_product_service(
    db,
    product_id: int
):


    print("\n========== DELETE PRODUCT ==========")

    product = db.query(Product).filter(
        Product.id == product_id
    ).first()

    if not product:

        return {
            "success": False,
            "message": "Product Not Found"
        }

    db.delete(product)

    db.commit()

    return {
        "success": True,
        "message": "Product Deleted Successfully"
    }


# =========================

# SEARCH PRODUCT

# =========================

def search_product_service(
    db,
    keyword: str
):


    print("\n========== SEARCH PRODUCT ==========")

    products = db.query(Product).filter(
        Product.title.contains(keyword)
    ).all()

    return products


# =========================

# PAGINATION

# =========================

def pagination_service(
    db,
    page: int,
    limit: int
):


    print("\n========== PAGINATION ==========")

    skip = (page - 1) * limit

    products = db.query(Product).offset(
        skip
    ).limit(
        limit
    ).all()

    return {
        "page": page,
        "limit": limit,
        "total_items": len(products),
        "data": products
    }

