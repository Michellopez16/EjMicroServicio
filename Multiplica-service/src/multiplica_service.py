from fastapi import FastAPI
from pydantic import BaseModel

class Operacion(BaseModel):
    a: float
    b: float

app = FastAPI()

@app.post("/multiplica")
def sumar(operacion: Operacion):
    return {"resultado": operacion.a * operacion.b}