import requests

def get_location(query):
    """
    Função para lidar com a requesição da API(http://ip-api.com/json/)
    tomando como argumentos a str query e retorna os dados em JSON.
    """
    url = f"http://ip-api.com/json/{query}"  #3th party API
    response = requests.get(url).json()    #data em formato JSON                           
    return response
