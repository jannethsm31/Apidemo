from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():

    return {"Hello": "World"}

@app.get("/v1/contactos")
async def get_contactos():
    response= []
    return response
    

git add .
git commit -m "Commit"
git push -u origin.main
