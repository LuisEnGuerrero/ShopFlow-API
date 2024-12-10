from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

# ---------------------------------------------------
# Schemas para Productos
# ---------------------------------------------------
class ProductoBase(BaseModel):
    nombre: str = Field(..., example="Laptop")
    descripcion: Optional[str] = Field(None, example="Una laptop de alta gama")
    precio: float = Field(..., ge=0, example=1200.99)
    stock: int = Field(..., ge=0, example=10)
    categoria: Optional[str] = Field(None, example="Tecnología")
    imagen_url: Optional[str] = Field(None, example="http://example.com/laptop.jpg")

class ProductoCreate(ProductoBase):
    """Modelo usado al crear un nuevo producto."""
    pass

class ProductoUpdate(ProductoBase):
    """Modelo usado para actualizar un producto."""
    nombre: Optional[str]
    precio: Optional[float]
    stock: Optional[int]

class ProductoDB(ProductoBase):
    """Modelo usado para la respuesta desde la base de datos."""
    id: str
    fecha_creacion: datetime
    ultima_actualizacion: datetime

# ---------------------------------------------------
# Schemas para Carrito
# ---------------------------------------------------
class CartItem(BaseModel):
    product_id: str = Field(..., example="64b1f0cd3f3c9bba1e2c1e5b")
    quantity: int = Field(..., ge=1, example=2)
    price: float = Field(..., ge=0, example=599.99)

class CartSchema(BaseModel):
    user_id: str = Field(..., example="64b1f0cd3f3c9bba1e2c1e5b")
    items: List[CartItem]
    total: Optional[float] = Field(0, example=1199.98, description="Total calculado automáticamente")

# ---------------------------------------------------
# Schemas para Visibilidad
# ---------------------------------------------------
class VisibilitySchema(BaseModel):
    product_id: str = Field(..., example="64b1f0cd3f3c9bba1e2c1e5b")
    is_visible: bool = Field(..., example=True)
