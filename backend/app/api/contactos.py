from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.config import ENVIRONMENT

from app.schemas.contactos import ContactoCreate, ContactoResponse

from app.services.contacto_service import crear_contacto

router = APIRouter(
    prefix="/api/v1",
    tags=["Contactos"] 
)

@router.get("/health")
def health():
    return {
        "status": "ok",
        "environment": ENVIRONMENT
    }
    
@router.post(
    "/contactos",
    response_model=ContactoResponse,
    status_code=201
)
def guardar_contacto(
    contacto: ContactoCreate,
    db: Session = Depends(get_db)
):
    crear_contacto(
        db=db,
        contacto=contacto
    )
    
    return {
        "message": "Formulario enviado correctamente"
    }