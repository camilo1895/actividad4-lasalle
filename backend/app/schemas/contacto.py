from pydantic import BaseModel, ConfigDict, EmailStr, Field


class ContactoCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    nombre: str = Field(min_length=1, max_length=100)
    correo: EmailStr = Field(max_length=254)
    asunto: str = Field(min_length=1, max_length=150)
    mensaje: str = Field(min_length=1, max_length=2000)


class ContactoResponse(BaseModel):
    id: int
    message: str
    