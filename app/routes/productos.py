from fastapi import APIRouter, HTTPException, status, Depends
from bson import ObjectId
from app.database import db
from app.schemas import ProductoCreate, ProductoUpdate, ProductoDB
from typing import List
from datetime import datetime

router = APIRouter(
    prefix="/productos",
    tags=["productos"]
)

# Crear un producto
@router.post("/", response_model=ProductoDB, status_code=status.HTTP_201_CREATED)
async def create_producto(producto: ProductoCreate):
    data = producto.dict()
    data["fecha_creacion"] = datetime.utcnow()
    data["ultima_actualizacion"] = datetime.utcnow()
    result = await db.productos_.insert_one(data)
    data["id"] = str(result.inserted_id)
    return data

# Obtener todos los productos
@router.get("/", response_model=List[ProductoDB])
async def get_all_productos():
    productos = await db.productos_.find().to_list(100)
    for producto in productos:
        producto["id"] = str(producto["_id"])
        del producto["_id"]
    return productos

# Obtener un producto por ID
@router.get("/{producto_id}", response_model=ProductoDB)
async def get_producto_by_id(producto_id: str):
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID inválido")
    producto = await db.productos_.find_one({"_id": ObjectId(producto_id)})
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    producto["id"] = str(producto["_id"])
    del producto["_id"]
    return producto

# Actualizar un producto
@router.put("/{producto_id}", response_model=ProductoDB)
async def update_producto(producto_id: str, updates: ProductoUpdate):
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID inválido")
    updates_data = {k: v for k, v in updates.dict().items() if v is not None}
    updates_data["ultima_actualizacion"] = datetime.utcnow()
    result = await db.productos_.update_one(
        {"_id": ObjectId(producto_id)}, {"$set": updates_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    producto = await db.productos_.find_one({"_id": ObjectId(producto_id)})
    producto["id"] = str(producto["_id"])
    del producto["_id"]
    return producto

# Eliminar un producto
@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_producto(producto_id: str):
    if not ObjectId.is_valid(producto_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID inválido")
    result = await db.productos_.delete_one({"_id": ObjectId(producto_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
