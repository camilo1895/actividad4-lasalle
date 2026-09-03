from pydantic import BaseModel, EmailStr, Field

class ContactoCreate(BaseModel):
    nombre: str = Field(
        min_length=1,
        max_length=100
        )
    
    correo: EmailStr
    
    asunto: str = Field(
        min_length=1,
        max_length=150
        )
    
    mensaje: str = Field(
        min_length=1
        )
    
    class ContactoResponse(BaseModel):
        mensaje: str