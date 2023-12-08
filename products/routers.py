from fastapi import APIRouter, HTTPException, status, Response
from products.models import Product
from users.routers import get_permission, get_users, get_user
from helpers.sendemail import send_email

router = APIRouter()

products = []


@router.post("/products/{user_id}")
def create_products(product: Product, user_id: int, response: Response):
    if not get_permission(user_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorized"
        )
    products.append(product)
    response.status_code = status.HTTP_201_CREATED
    return {
        'detail': products
    }


@router.get("/products/{sku}/{user_id = None}")
def consulting_products_by_sku(sku: str,  user_id: int = None):
    product = None
    for item in products:
        if item.sku == sku:
            if not get_permission(user_id):
                item.consulted += 1
            product = item
    return {
        'detail': product
    }


@router.put("/products/{sku}/{user_id}")
def update_consulting_user(sku: str, product: Product, user_id: int):
    if not get_permission(user_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorized"
        )
    product_update = None
    for item in products:
        if item.sku == sku:
            item.name = product.name
            item.price = product.price
            item.brand = product.brand
            product_update = item
            break
    send_email(product_update, get_user(user_id), get_users())
    return {
        'detail': product_update
    }


@router.delete("/products/{sku}/{user_id}")
def delete_user(sku: str, user_id: int):
    if not get_permission(user_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorized"
        )
    for item in products:
        if item.sku == sku:
            products.remove(item)
    return {
        'detail': products
    }


@router.get("/products/{user_id}")
def list_products(user_id: int):
    if not get_permission(user_id):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User Unauthorized"
        )
    return {
        'detail': products
    }
