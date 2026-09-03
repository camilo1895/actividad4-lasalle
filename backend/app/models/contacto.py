from sqlalchemy import Column, Integer, String, BigInteger, Text, DateTime, ForeignKey

from sqlalchemy.sql import func

from app.core.database import Base

class Contacto(Base):
    __tablename__ = "contactos"

    id = Column(
        BigInteger,
        primary_key=True,
        index=True
        )
    
    nombre = Column(
        String(100),
        nullable=False
        )
    
    asunto = Column(
        String(150),
        nullable=False
        )
    
    email = Column(
        String(254),
        nullable=False,
        unique=True
        )
    
    mensaje = Column(
        Text,
        nullable=False
        )
    
    fecha_creacion = Column(
        DateTime(timezone=True),
        server_default=func.now()
        )