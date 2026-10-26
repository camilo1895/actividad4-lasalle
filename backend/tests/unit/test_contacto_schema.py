import pytest
from pydantic import ValidationError
from app.schemas.contacto import ContactoCreate

DATOS = {
    "nombre": "Ana Prueba",
    "correo": "ana.prueba@example.com",
    "asunto": "CP-UNI-01",
    "mensaje": "Solicito información",
}


def test_cp_uni_01_datos_validos_se_aceptan():
    contacto = ContactoCreate(**DATOS)
    assert contacto.nombre == DATOS["nombre"]
    assert contacto.correo == DATOS["correo"]
    assert contacto.asunto == DATOS["asunto"]
    assert contacto.mensaje == DATOS["mensaje"]


def test_cp_uni_02_nombre_de_espacios_se_rechaza():
    with pytest.raises(ValidationError) as error:
        ContactoCreate(**{**DATOS, "nombre": "   "})
    assert "nombre" in str(error.value)
