import requests

URI = "https://8000-jannethsm31-apidemo-f9eh24u6vlu.ws-us105.gitpod.io/v1/contactos"

response= requests.get(URI)

print(f"GET: {response.text}")
print(f"GET: {response.status_code}")

data= {"id":"4",
        "nombre": "Prueba", 
        "email": "prueba@email.com"}

response = requests.post(URI, json=data)
print(f"POST: {response.text}")
print(f"POST: {response.status_code}")