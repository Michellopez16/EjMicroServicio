from fastapi import FastAPI, Request, HTTPException
import httpx
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Direcciones y puertos de los microservicios
SERVICES = {
    "suma": "http://suma_service:8001/suma",
    "resta": "http://resta_service:8002/resta",
    "multiplica": "http://multiplica_service:8003/multiplica",
    "divide": "http://divide_service:8004/divide"
}

# Configurar CORS para este servicio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/{service_name}")
async def perform_operation(service_name: str, request: Request):
    if service_name not in SERVICES:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")

    # Obtener la URL completa del servicio
    service_url = SERVICES[service_name]
    body = await request.body()

    # Usar httpx para enviar la solicitud al servicio correspondiente
    async with httpx.AsyncClient() as client:
        try:
            # Realizar la petición al servicio correspondiente
            resp = await client.post(service_url, content=body)
            # Devolver la respuesta del microservicio
            return resp.json()
        except httpx.RequestError as exc:
            # Si hay un error en la solicitud, levantar una excepción HTTP
            raise HTTPException(status_code=500, detail=str(exc))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)