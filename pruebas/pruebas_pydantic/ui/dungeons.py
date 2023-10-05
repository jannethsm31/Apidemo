import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"

response = requests.get(URI)

#print(f"GET: {response.text}")

response_json = json.loads(response.text)

print(f"1.{response_json['results'][0]['name']}")
print(f"2.{response_json['results'][1]['name']}")
