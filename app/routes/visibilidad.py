from fastapi import APIRouter, HTTPException
from app.database import db
from app.schemas import VisibilitySchema

router = APIRouter()

@router.get("/visibilidad/{product_id}", response_model=VisibilitySchema)
async def get_visibility(product_id: str):
    """
    Obtener el estado de visibilidad de un producto.
    """
    visibility = await db["visibilidad"].find_one({"product_id": product_id})
    if not visibility:
        raise HTTPException(status_code=404, detail="Visibilidad no encontrada")
    return visibility

@router.put("/visibilidad/{product_id}", response_model=VisibilitySchema)
async def update_visibility(product_id: str, visibility: VisibilitySchema):
    """
    Actualizar la visibilidad de un producto.
    """
    existing_visibility = await db["visibilidad"].find_one({"product_id": product_id})
    if not existing_visibility:
        raise HTTPException(status_code=404, detail="Visibilidad no encontrada")
    await db["visibilidad"].update_one(
        {"product_id": product_id},
        {"$set": {"is_visible": visibility.is_visible}}
    )
    return visibility
