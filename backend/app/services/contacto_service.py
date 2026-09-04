from sqlalchemy.orm import Session

from app.models.contacto import Contacto
from app.schemas.contacto import ContactoCreate

def crear_contacto(
    db: Session,
    contacto: ContactoCreate
    ):
        nuevo_contacto = Contacto(
            nombre=contacto.nombre,
            correo=contacto.correo,
            asunto=contacto.asunto,
            mensaje=contacto.mensaje
        )
        
        db.add(nuevo_contacto)
        db.commit()
        dm.refresh(nuevo_contacto)
        
        return nuevo_contacto