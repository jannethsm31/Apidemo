from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

upload_folder = "static"

@app.get("/")
async def main():
  content = """
  <body>
  <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
  <input name="files" type="file" multiple>
  <input type="submit">
  </form>
  </body>
  """
  return HTMLResponse(content=content)

@app.post("/uploadfiles/")
async def upload_files(files: list[UploadFile] = File(...)):
  for file in files:
    # Verificamos que el archivo sea una imagen
    if file.content_type.startswith("image"):
      upload_folder = "static/images"
    # Si no es una imagen, es un pdf
    else: 
      upload_folder = "static/pdf"

    # Crear la carpeta de destino si no existe
    os.makedirs(upload_folder, exist_ok=True)

    # Generar el nombre del archivo en la carpeta de destino
    file_path = os.path.join(upload_folder, file.filename)

    # Guardar el archivo en la carpeta de destino
    file_path = os.path.join(upload_folder, file.filename)

    # Guardar el archivo en la carpeta de destino
    with open(file_path, "wb") as f:
      f.write(file.file.read())

  return {"message": "Archivos subidos exitosamente"}




  
