from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.contactos import router

from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Formulario de Contacto La Salle API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)