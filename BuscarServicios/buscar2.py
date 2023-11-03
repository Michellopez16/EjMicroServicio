import docker

# Inicializar el cliente de Docker
client = docker.from_env()

# Función para obtener la lista de contenedores en una red específica
def find_services_in_network(network_name):
    # Encontrar la red
    network = client.networks.get(network_name)

    # Obtener los contenedores conectados a la red
    containers = network.containers
    
    # Extraer los nombres de los servicios
    service_names = [container.name for container in containers]
    
    return service_names

# Nombre de la red a inspeccionar
network_name = "ejmicroservicio_calculadora-net"

# Encontrar los servicios
services = find_services_in_network(network_name)
print("Servicios encontrados en la red:", services)