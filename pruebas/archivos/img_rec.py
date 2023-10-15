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

            # Abre la imagen para realizar el recorte
            with Image.open(file_path) as img:
                # Coordenadas de la región a recortar (por ejemplo, x1, y1, x2, y2)
                x1, y1, x2, y2 = 100, 100, 300, 300

                # Recorta la región especificada
                cropped_img = img.crop((x1, y1, x2, y2))

                # Guarda la imagen recortada en la misma ruta
                cropped_img.save(file_path)

        # Si no es una imagen, asumimos que es un PDF
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
