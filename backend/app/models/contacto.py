from sqlalchemy import BigInteger, Column, DateTime, String, Text

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
    
    correo = Column(
        String(254),
        nullable=False,
        )
    
    mensaje = Column(
        Text,
        nullable=False
        )
    
    created_at  = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        )