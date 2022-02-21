import requests

def get_location(query):
    url = f"http://ip-api.com/json/{query}" 
    response = requests.get(url).json()                              
    return response