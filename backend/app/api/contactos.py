from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from app.core.database import get_db
from app.core.config import ENVIRONMENT

from app.schemas.contacto import ContactoCreate, ContactoResponse

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
    
@router.post("/contactos",
    response_model=ContactoResponse,
    status_code=201)
def guardar_contacto(
    contacto: ContactoCreate,
    db: Session = Depends(get_db)
):
    try:
        nuevo_contacto = crear_contacto(
            db=db,
            contacto=contacto,
        )
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=500,
            detail="No fue posible guardar el contacto.",
        ) from error

    return ContactoResponse(
        id=nuevo_contacto.id,
        message="Mensaje enviado correctamente.",
    )