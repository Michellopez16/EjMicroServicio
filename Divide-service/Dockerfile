# Use the official Python image that includes all dependencies
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY ./src .

# Exponer el puerto en el que el servicio se ejecutará
EXPOSE 8004

# Specify the command to run on container start
CMD ["uvicorn", "divide_service:app", "--host", "0.0.0.0", "--port", "8004"]