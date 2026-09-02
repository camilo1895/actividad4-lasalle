from fastapi import FastAPI

app = FastAPI(
    title="Formulario de Contacto La Salle API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "API Formulario de Contacto La Salle"
    }