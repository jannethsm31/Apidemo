from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from PIL import Image
import os
import shutil

app = FastAPI()

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
        # Verifica si el archivo es una imagen
        if file.content_type.startswith("image"):
            upload_folder = "static/images"
            
            # Guarda el archivo en la carpeta de destino
            file_path = os.path.join(upload_folder, file.filename)

            with open(file_path, "wb") as f:
                f.write(file.file.read())

            # Gira la imagen en sentido contrario a las agujas del reloj (90 grados)
            with Image.open(file_path) as img:
                img = img.rotate(90, expand=True)
                
                # Guarda la imagen rotada
                img.save(file_path)
                
        # Si no es una imagen, asumimos que es un pdf
        else:
            upload_folder = "static/pdf"

            # Crear la carpeta de destino si no existe
            os.makedirs(upload_folder, exist_ok=True)

            # Generar el nombre del archivo en la carpeta de destino
            file_path = os.path.join(upload_folder, file.filename)

            # Guardar el archivo en la carpeta de destino
            with open(file_path, "wb") as f:
                f.write(file.file.read())

    return {"message": "Archivos subidos exitosamente"}
