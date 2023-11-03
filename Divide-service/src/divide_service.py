from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

class Operacion(BaseModel):
    a: float
    b: float

app = FastAPI()

@app.post("/divide")
def dividir(operacion: Operacion):
    if operacion.b == 0:
        return JSONResponse(content={"error": "No se puede dividir por cero"}, status_code=400)
    return {"resultado": operacion.a / operacion.b}