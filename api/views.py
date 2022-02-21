# Django
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Myserializer
import requests
from . requestapi import get_location


@api_view(['GET'])
def location_detail(request): 
    """
    Recebe a requesição e retorna os dados em JSON com 
    o ip (query) fornecido.
    """
    serializer = Myserializer(data=request.GET)    # Passe os dados da solicitação para o Mtserializer()       
    serializer.is_valid()                          # Retorna True se os campos forem validos              
    query = serializer.validated_data['query']  
    ip_info = get_location(query)   # Chama a função get_location que consulta a API
    return Response(ip_info)


