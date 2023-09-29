from fastapi import FastAPI
from csv_to_json import csv_to_json


app = FastAPI()


@app.get("/")
async def read_root():

    return {"Hello": "World"}

@app.get("/v1/contactos")
async def get_contactos():
    input_csv_file = 'contactos.csv'
    output_json_file = 'contactos.json'
    csv_to_json(input_csv_file, output_json_file)

    return {"message": "Datos convertidos de CSV a JSON"}

    #with open(input_csv_file, mode='r') as csv_file:

    #    csv_reader = csv.DictReader(csv_file)
    #    data = [row for row in csv_reader]

    #with open(output_json_file, 'w') as json_file:
    #    json.dump(data, json_file)

    


 

#git add .
#git commit -m "Commit"
#git push -u origin.main
