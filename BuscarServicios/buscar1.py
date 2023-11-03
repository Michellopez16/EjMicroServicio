import subprocess
import json

# Función para obtener la lista de contenedores que corren en una red específica
def find_services_in_network(network_name):
    # Ejecutar el comando `docker network inspect`
    result = subprocess.run(
        ["docker", "network", "inspect", network_name], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )
    
    # Revisar si hubo errores
    if result.returncode != 0:
        print(f"Error: {result.stderr.decode('utf-8')}")
        return []

    # Cargar el resultado como JSON
    data = json.loads(result.stdout)

    # Obtener la lista de contenedores conectados a la red
    containers = data[0].get("Containers", {})
    
    # Extraer los nombres de los servicios a partir de los contenedores
    service_names = [container["Name"] for container_id, container in containers.items()]
    
    return service_names

# Nombre de la red a inspeccionar
network_name = "ejmicroservicio_calculadora-net"

# Encontrar los servicios
services = find_services_in_network(network_name)
print("Servicios encontrados en la red:", services)
