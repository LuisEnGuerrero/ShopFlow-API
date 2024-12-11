# ShopFlow API

Bienvenido a **ShopFlow API**, una API RESTful construida con FastAPI para manejar productos, carritos de compras y visibilidad en una tienda en línea. Este proyecto está diseñado para integrarse con aplicaciones frontend modernas, como React, y utiliza MongoDB como base de datos.

## 🚀 Funcionalidades

- **Gestión de Productos**: CRUD completo para productos.
- **Gestión de Carritos**: Añadir, actualizar y eliminar productos del carrito.
- **Gestión de Visibilidad**: Controlar la visibilidad de los productos en la tienda.
- **Pruebas y Monitoreo**: Endpoints para verificar la conexión a la base de datos y la salud del sistema.
- **Escalabilidad Modular**: Arquitectura diseñada para facilitar futuras expansiones.

## 📋 Requisitos Previos

Antes de empezar, asegúrate de tener instalado:

- Python 3.9 o superior
- MongoDB Atlas o una instancia local de MongoDB
- `pip` para instalar dependencias

## 🛠️ Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tuusuario/shopflow-api.git
cd shopflow-api
```
Crea y activa un entorno virtual:


```bash
python -m venv env
source env/bin/activate  # En Windows: .\env\Scripts\activate
```
Instala las dependencias:


```bash
pip install -r requirements.txt
```
Configura el archivo .env: Crea un archivo .env en el directorio raíz y agrega las siguientes variables:

```makefile
MONGODB_URI=<tu-cadena-de-conexion-de-MongoDB>
DB_NAME=shopflow
```

▶️ Uso
Inicia el servidor:

```bash
uvicorn app.main:app --reload
```
El Servidor cargará en: http://localhost:8000/

Accede a la documentación interactiva:

### Swagger UI
http://localhost:8000/Docs/


### 📂 Estructura del Proyecto
```bash
ShopFlow API/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── schemas.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── productos.py
│   │   ├── carrito.py
│   │   ├── visibilidad.py
├── .env
├── requirements.txt
```

### 📦 Dependencias
FastAPI: Framework para construir APIs rápidas y modernas.
Uvicorn: Servidor ASGI para correr la aplicación.
Motor: Cliente asincrónico para MongoDB.
Pydantic: Validación de datos y esquemas.

### 🔧 Configuración Adicional
MongoDB Atlas: Asegúrate de configurar la colección productos_ en tu base de datos para iniciar correctamente.
Pruebas: Puedes usar herramientas como Postman para realizar pruebas de los endpoints.

### 🤝 Contribuciones
Si deseas contribuir, por favor abre un issue o un pull request. Cualquier ayuda es bienvenida.

### 📝 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más información.


### Indicaciones Finales

1. Guarda el archivo `README.md` en el directorio raíz del proyecto.
2. Sube todo el proyecto a tu repositorio de GitHub, incluyendo este archivo.
3. Verifica que toda la estructura esté correctamente documentada en tu repositorio remoto.

