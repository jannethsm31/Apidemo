import requests
import json




URI_CLASSES = "https://cat-fact.herokuapp.com/facts/random"
URI_BASE_CLASS = "https://cat-fact.herokuapp.com"


print(f"GET: {response.text}")
response_json = json.loads(response.text)
print(f"{response_json['text'][10]['']}")




