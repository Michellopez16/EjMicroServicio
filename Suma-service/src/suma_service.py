# suma_service.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Operacion(BaseModel):
    a: float
    b: float



app = FastAPI()

# Configurar CORS para este servicio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/suma")
def sumar(operacion: Operacion):
    return {"resultado": operacion.a + operacion.b}