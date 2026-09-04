from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from app.core.config import DATABASE_URL


# Motor principal de SQLAlchemy.
# Administra las conexiones entre FastAPI y PostgreSQL.
engine = create_engine(
    DATABASE_URL,

     # Comprueba que una conexión siga activa antes de utilizarla.
    # Ayuda cuando PostgreSQL cierra conexiones inactivas.
    pool_pre_ping=True,
)


# Fábrica utilizada para crear una sesión de base de datos
# independiente para cada petición.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Clase base de la que heredan los modelos de SQLAlchemy.
# Permite registrar tablas como el modelo Contacto.
Base = declarative_base()

def get_db():

    """
    Entrega una sesión de base de datos a una ruta de FastAPI
    y garantiza que la sesión se cierre al terminar la petición.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()