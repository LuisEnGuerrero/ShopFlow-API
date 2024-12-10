from fastapi import APIRouter, HTTPException, Depends
from app.database import db
from app.schemas import CartSchema, CartItem

router = APIRouter()

@router.get("/carrito/{user_id}", response_model=CartSchema)
async def get_cart(user_id: str):
    """
    Obtener el carrito de compras de un usuario.
    """
    cart = await db["carrito"].find_one({"user_id": user_id})
    if not cart:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    return cart

@router.post("/carrito", response_model=CartSchema)
async def create_cart(cart: CartSchema):
    """
    Crear un nuevo carrito para un usuario.
    """
    existing_cart = await db["carrito"].find_one({"user_id": cart.user_id})
    if existing_cart:
        raise HTTPException(status_code=400, detail="El carrito ya existe")
    cart_data = cart.dict()
    cart_data["total"] = sum(item.quantity * item.price for item in cart.items)
    await db["carrito"].insert_one(cart_data)
    return cart_data

@router.put("/carrito/{user_id}", response_model=CartSchema)
async def update_cart(user_id: str, updated_cart: CartSchema):
    """
    Actualizar el carrito de un usuario.
    """
    cart = await db["carrito"].find_one({"user_id": user_id})
    if not cart:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    updated_cart_data = updated_cart.dict()
    updated_cart_data["total"] = sum(item.quantity * item.price for item in updated_cart.items)
    await db["carrito"].replace_one({"user_id": user_id}, updated_cart_data)
    return updated_cart_data

@router.delete("/carrito/{user_id}")
async def delete_cart(user_id: str):
    """
    Eliminar el carrito de un usuario.
    """
    result = await db["carrito"].delete_one({"user_id": user_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Carrito no encontrado")
    return {"message": "Carrito eliminado exitosamente"}
