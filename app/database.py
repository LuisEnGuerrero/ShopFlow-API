import motor.motor_asyncio
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

async def init_db():
    # Inicializar la base de datos (si necesitas configuraciones iniciales)
    try:
        await db.list_collection_names()  # Comprobar la conexión
        print(f"Conexión exitosa a la base de datos: {DB_NAME}")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {str(e)}")
        raise e

