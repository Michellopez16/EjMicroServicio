# Utilizar la imagen base oficial de Nginx
FROM nginx:alpine

# Copiar el archivo HTML estático al directorio de Nginx
COPY ./src /usr/share/nginx/html

EXPOSE 80
# No es necesario especificar un CMD porque la imagen base ya tiene un proceso predeterminado para correr Nginx