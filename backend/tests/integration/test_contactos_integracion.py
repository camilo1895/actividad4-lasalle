"""CP-INT-02: rechazar un nombre vacío sin guardar otro contacto."""

import json
import os
from uuid import uuid4

from dotenv import dotenv_values
from fastapi.testclient import TestClient
from sqlalchemy import delete, select
from sqlalchemy.engine import make_url


def test_nombre_vacio_no_se_guarda():
    # Lee la configuración de pruebas.
    configuracion = dotenv_values(".env.test")
    conexion = configuracion.get("DATABASE_URL")
    assert conexion, "Falta DATABASE_URL en .env.test."

    # Comprueba que se use la base local de pruebas.
    url = make_url(conexion)
    assert url.drivername == "postgresql+psycopg"
    assert url.host in {"localhost", "127.0.0.1", "::1"}
    assert url.database == "lasalle_contacto_test"

    # Configura el ambiente antes de cargar la aplicación.
    os.environ["ENVIRONMENT"] = "TEST"
    os.environ["DATABASE_URL"] = conexion
    os.environ["CORS_ORIGINS"] = "http://localhost:3001"

    from app.main import app
    from app.core.database import SessionLocal
    from app.models.contacto import Contacto

    # Identifica los datos de esta prueba.
    asunto = f"CP-INT-02-{uuid4().hex}"
    print(f"Identificador de la ejecución: {asunto}")
    
    datos = {
        "nombre": "Control de integracion",
        "correo": "integracion@example.com",
        "asunto": asunto,
        "mensaje": "Registro sintetico para comprobar persistencia.",
    }

    def consultar_contactos():
        # Consulta los registros asociados al asunto.
        with SessionLocal() as db:
            consulta = select(
                Contacto.id,
                Contacto.nombre,
                Contacto.correo,
                Contacto.asunto,
                Contacto.mensaje,
            ).where(Contacto.asunto == asunto)

            return [
                dict(fila)
                for fila in db.execute(consulta).mappings()
            ]

    try:
        # Inicia la aplicación sin levantar Uvicorn.
        with TestClient(app) as cliente:
            assert consultar_contactos() == []
            print("[OK] Estado inicial: no existen registros del caso.")

            # Envía un contacto válido.
            respuesta = cliente.post("/api/v1/contactos", json=datos)
            assert respuesta.status_code == 201
            print("[OK] Contacto válido: respuesta HTTP 201.")

            # Comprueba que se guardó con los datos correctos.
            antes = consultar_contactos()
            assert antes == [{"id": respuesta.json()["id"], **datos}]
            print(
                f"[OK] Persistencia: una fila con id {antes[0]['id']} "
                "y todos los datos correctos."
            )

            # Envía otro contacto con el nombre vacío.
            datos_invalidos = {**datos, "nombre": "   "}

            print("\n--- Solicitud inválida ---")
            print(json.dumps(datos_invalidos, indent=2, ensure_ascii=False))

            respuesta = cliente.post(
                "/api/v1/contactos",
                json=datos_invalidos,
            )

            # Muestra la respuesta real antes de comprobarla.
            print("\n--- Respuesta de la API ---")
            print("Código esperado: 422")
            print(f"Código obtenido: {respuesta.status_code}")
            print(json.dumps(respuesta.json(), indent=2, ensure_ascii=False))


            # Comprueba el rechazo y el campo señalado.
            assert respuesta.status_code == 422, (
                f"Se esperaba HTTP 422, pero se recibió {respuesta.status_code}."
            )
            

            # Comprueba que el error corresponda al nombre.
            errores = respuesta.json().get("detail", [])

            assert any(
                error.get("loc") == ["body", "nombre"]
                for error in errores
            ), "La API no identificó el error en el campo nombre."

            print("[OK] La API rechazó el nombre de tres espacios.")

           # Compara los registros antes y después del envío inválido.
            despues = consultar_contactos()
            
            print("\n--- Verificación en PostgreSQL ---")
            print("Antes del envío inválido:")
            print(json.dumps(antes, indent=2, ensure_ascii=False))
            print("Después del envío inválido:")
            print(json.dumps(despues, indent=2, ensure_ascii=False))
            
            assert despues == antes, (
                "Los registros cambiaron después de enviar los datos inválidos."
            )
            
            print("[OK] El contacto de control sigue intacto y no hay registros adicionales.")

    finally:
        # Elimina únicamente los datos de esta prueba.
        with SessionLocal() as db:
            db.execute(
                delete(Contacto).where(Contacto.asunto == asunto)
            )
            db.commit()
        print("[OK] Limpieza completada para los registros de este caso.")