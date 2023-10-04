from fastapi import FastAPI
from pydantic import BaseModel

"""
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict 
"""


from pydantic import EmailStr
from datetime import datetime

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
    datos= []
    with open('contactos.csv', 'r') as file:
        lector = csv.DictReader(file)
        for row in lector:
            datos.append(row)
    return datos

@app.post("/v1/contactos", status_code=status.HTTP_201_CREATED, summary="Endpoint para enviar datos")
def add_contactos(post:Post):

    """
    # Endpoint para enviar datos de la API

    ## 1.- Status Codes:
    * 201 - Código de confirmación de agregar nuevo elemento

    ## 2.- Data:
    * nombre: str
    * email: EmailStr
    """
    with open('contactos.csv', 'a', newline="") as file:
        fieldnames = ["id", "nombre", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        row = post.model_dump()
        writer.writerow(row)
    return row, {"datetime": datetime.now()}



@app.get("/v1/contactos/{id}", status_code=status.HTTP_200_OK, summary="Endpoint para listar datos")
def get_contactosid(id:str):

    """
    # Endpoint para obtener datos específicos de la API

    ## 1.- Status Codes:
    * 200 - Código de confirmación
    * 404 - Código de error
    """
    with open('contactos.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['id'] == id:
                return row

    return row, {"datetime": datetime.now()}



















    
# MAIN.PY INICIAL
"""
    """
    Actividades (TODO):
    read contactos.csv
    JSON enconde contactos.csv
    save in response
    """

from fastapi import FastAPI, status # Importa la variable de estados
from csv_to_json import csv_to_json
from pydantic import BaseModel
from datetime import datetime
import csv


app = FastAPI()

# Clase modelo
class Post(BaseModel):
    nombre: str
    email: str

 @app.get("/") # Asignación predeterminada
 @app.get("/", status_code=202) # Asignación sin librería, sólo poniendo el número
 @app.get("/", status_code=status.HTTP_200_OK) # Asignación a través de la librería, permitiendo desplegar opciones de código
 Agrega una descripción y resumen en la documentación

"""
@app.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Endpoint raíz de la API Contactos",
    summary="Endpoint raíz"
)
"""
@app.get("/", status_code=status.HTTP_200_OK, summary="Endpoint raíz")
def read_root():
# async def root(): # Convierte la función en asíncrona
# Agregamos documentación
    """
    #Endpoint raíz

    ## 1- Status codes:
    * 200 - Código de confirmación
    * 289 - Código de muestra
    * 334 - Otro código de muestra
    """

    return {"Hello":"World"}

@app.get("/v1/contactos", status_code=status.HTTP_200_OK, summary="Endpoint para listar datos")
def get_contactos():
    """
    # Endpoint para obtener datos de la API

    ## 1.- Status codes:
    * 200 - Código de confirmación
    """
    datos = []
    with open('contactos.csv', 'r') as file:
        lector = csv.DictReader(file)
        for row in lector:
            datos.append(row)
    return datos

# Forma 1

 @app.post("/v1/contactos", status_code=status.HTTP_201_CREATED, summary="Endpoint para enviar datos")
 def add_contactos(nombre:str, email:str):
    """
    # Endpoint para enviar datos de la API

    ## 1.- Status codes:
    * 201 - Código de confirmación de agregar nuevo elemento

    ## 2.- Data:
    * nombre: str
    * email: str
    """
    with open('contactos.csv', 'a', newline="") as file:
        fieldnames = ["nombre", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        row = {"nombre": nombre, "email": email}  #  Uso de diccionario
        writer.writerow(row)
    return row, {"datetime":datetime.now()}  # Mensaje de confirmación


# Forma 2
@app.post("/v1/contactos", status_code=status.HTTP_201_CREATED, summary="Endpoint para enviar datos")
def add_contactos(post:Post):
    """
    # Endpoint para enviar datos de la API

    ## 1.- Status codes:
    * 201 - Código de confirmación de agregar nuevo elemento

    ## 2.- Data:
    * nombre: str
    * email: str
   """
    with open('contactos.csv', 'a', newline="") as file:
        fieldnames = ["nombre", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        row = post.dict() # Uso de diccionario
        writer.writerow(row)
    return row, {"datetime":datetime.now()} # Mensaje de confirmación

@app.get("/")
async def read_root():

    return {"Hello": "World"}

@app.get("/v1/contactos")
async def get_contactos():
    input_csv_file = 'contactos.csv'
    output_json_file = 'contactos.json'
    csv_to_json(input_csv_file, output_json_file)

    return {"message": "Datos convertidos de CSV a JSON"}

    with open(input_csv_file, mode='r') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]

    with open(output_json_file, 'w') as json_file:
       json.dump(data, json_file)
"""


