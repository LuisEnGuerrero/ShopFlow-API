from fastapi import FastAPI
from app.routes import productos, carrito, visibilidad
from app.database import init_db, db


# Crear instancia de la aplicación FastAPI
app = FastAPI(
    title="ShopFlow API",
    description="API para gestionar productos y carritos en una tienda en línea.",
    version="0.1.0",
    contact={
        "name": "Luis Enrique Guerrero",
        "email": "LuisEnGuerrero@yahoo.com"
    },
)

# Inicializar la base de datos al inicio de la aplicación
@app.on_event("startup")
async def startup_event():
    await init_db()

# Incluir las rutas principales
app.include_router(productos.router, prefix="/api", tags=["Productos"])
app.include_router(carrito.router, prefix="/api", tags=["Carrito"])
app.include_router(visibilidad.router, prefix="/api", tags=["Visibilidad"])

# Ruta de prueba para verificar la conexión a la base de datos
@app.get("/api/test-db", tags=["Database"])
async def test_database():
    try:
        collection_names = await db.list_collection_names()
        return {"collections": collection_names}
    except Exception as e:
        return {"error": str(e)}

# Ruta de inicio para verificar la salud del sistema
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Bienvenido a ShopFlow API. Todo está funcionando correctamente."}
