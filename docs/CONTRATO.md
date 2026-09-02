# Contrato del proyecto

## Stack

- Next.js
- FastAPI
- PostgreSQL

## Campos

- nombre: string, requerido, max 100
- correo: email, requerido, max 254
- asunto: string, requerido, max 150
- mensaje: string, requerido, max 2000

## Endpoints

POST /api/v1/contactos
GET /api/v1/health

## Bases de datos

DEV: lasalle_contacto_dev
TEST: lasalle_contacto_test
PROD: lasalle_contacto_prod

## Puertos

DEV:
Frontend 3000
Backend 8000

TEST:
Frontend 3001
Backend 8001
