import requests
import json

"""
Al seleccionar uno de los personajes con numero y 
que este muestre las proficiencies que este tiene

"""

URI_CLASSES = "https://www.dnd5eapi.co/api/classes"
URI_BASE_CLASS = "https://www.dnd5eapi.co"

# Función para obtener las proficiencias de un personaje específico
def obtener_proficiencias(personaje):
    # Realizar una solicitud GET para obtener detalles del personaje específico
    response = requests.get(f"{URI_BASE_CLASS}{personaje['url']}")
    
    # Verificar si la solicitud a la API fue exitosa
    if response.status_code == 200:
        # Analizar la respuesta JSON
        character_details = json.loads(response.text)
        
        # Obtener las proficiencias del personaje
        proficiencies = character_details['proficiencies']
        
        # Imprimir el nombre del personaje
        print(f"Proficiencias para el personaje: {personaje['name']}")
        
        # Enumerar e imprimir las proficiencias
        for i, proficiency in enumerate(proficiencies, start=1):
            print(f"{i}. {proficiency['name']}")
    else:
        print("Error al obtener los datos de la API")

# Obtener la lista de clases (personajes)
response = requests.get(URI_CLASSES)

# Verificar si la solicitud a la API fue exitosa
if response.status_code == 200:
    # Analizar la respuesta JSON
    response_json = json.loads(response.text)
    
    # Obtener la lista de personajes (clases)
    characters = response_json['results']
    
    # Enumerar e imprimir los nombres de los personajes (clases)
    for i, character in enumerate(characters, start=1):
        print(f"{i}. {character['name']}")
    
    # Solicitar al usuario que seleccione un número de personaje (clase)
    numero_seleccionado = int(input("Selecciona un número de personaje para ver sus proficiencias: "))
    
    # Verificar si el número seleccionado es válido
    if 1 <= numero_seleccionado <= len(characters):
        personaje_seleccionado = characters[numero_seleccionado - 1]
        obtener_proficiencias(personaje_seleccionado)
    else:
        print("Número de personaje no válido")
else:
    print("Error al obtener los datos de la API")

"""
print(f"GET: {response.text}")
response_json = json.loads(response.text)
print(f"{response_json['results'][10]['name']}")
"""

"""
# Verificar si la solicitud a la API fue exitosa
if response.status_code == 200:
    # Analizar la respuesta JSON
    response_json = json.loads(response.text)
    
    # Obtener la lista de clases
    classes = response_json['results']
    
    # Enumerar e imprimir los nombres de las clases
    for i, character_class in enumerate(classes, start=1):
        print(f"{i}. {character_class['name']}")
else:
    print("Error al obtener los datos de la API")

"""
