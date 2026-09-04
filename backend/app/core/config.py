import os
from pathlib import Path

from dotenv import load_dotenv

# Ruta absoluta de la carpeta backend.
# Se utiliza para localizar los archivos .env sin depender
# de la carpeta desde la que se ejecute FastAPI.
BACKEND_DIR = Path(__file__).resolve().parents[2]


# Ambiente en el que se ejecuta la aplicación.
# Si APP_ENV no está definida, se usa development.
APP_ENV = os.getenv("APP_ENV", "development").lower()

# Archivos de variables utilizados solamente en local.
# Producción no carga un archivo: recibe las variables desde Render.
ENV_FILES = {
    "development": ".env.dev",
    "test": ".env.test",
}

# Selecciona el archivo correspondiente al ambiente actual.
env_file = ENV_FILES.get(APP_ENV)

if env_file:
    # Carga las variables locales sin sobrescribir las variables
    # que ya estén definidas en el sistema operativo.
    load_dotenv(
        BACKEND_DIR / env_file,
        override=False,
    )


# Se vuelve a leer APP_ENV porque también puede estar definida
# dentro del archivo local que acabamos de cargar.
APP_ENV = os.getenv("APP_ENV", APP_ENV).lower()


# Evita iniciar la aplicación con un nombre de ambiente incorrecto.
if APP_ENV not in {"development", "test", "production"}:
    raise RuntimeError(
        "APP_ENV debe ser development, test o production"
    )


# Dirección utilizada por SQLAlchemy para conectarse a PostgreSQL.
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError(
        f"Falta DATABASE_URL para el ambiente {APP_ENV}"
    )


# Lista de direcciones web autorizadas para consultar la API
# desde un navegador.
cors_value = os.getenv("CORS_ORIGINS")

if not cors_value:
    raise RuntimeError(
        f"Falta CORS_ORIGINS para el ambiente {APP_ENV}"
    )


# Permite configurar varios orígenes separados por comas.
# Ejemplo: http://localhost:3000,http://localhost:3001
CORS_ORIGINS = [
    origin.strip()
    for origin in cors_value.split(",")
    if origin.strip()
]

# Nombre temporal utilizado por la ruta health actual.
# Más adelante la ruta puede importar APP_ENV directamente.
ENVIRONMENT = APP_ENV