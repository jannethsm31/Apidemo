from pydantic import EmailStr, BaseModel
from datetime import datetime
from fastapi import FastAPI, status

app = FastAPI()

class Post(BaseModel):
    id: int
    nombre: str
    email: EmailStr

class Update(BaseModel):
    nombre: str
    email: EmailStr
    
@app.get("/v1/contactos", status_code=status.HTTP_200_OK, summary="Endpoint para listar datos")
def get_contactos():
    """
    # Endpoint para obtener datos de la API

    ## 1.- Status Codes:
    * 200 - Código de OK
    """
    datos = []
    with open('contactos.csv', 'r') as file:
        lector = csv.DictReader(file)
        for row in lector:
            datos.append(row)
    return datos

@app.post("/v1/contactos", status_code=status.HTTP_201_CREATED, summary="Endpoint para enviar datos")
def add_contactos(post: Post):
    """
    # Endpoint para enviar datos de la API

    ## 1.- Status Codes:
    * 201 - Código de confirmación de agregar nuevo elemento

    ## 2.- Data:
    * id: int
    * nombre: str
    * email: EmailStr
    """
    with open('contactos.csv', 'a', newline="") as file:
        fieldnames = ["id", "nombre", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        row = dict(post)
        writer.writerow(row)
    return row, {"datetime": datetime.now()}
