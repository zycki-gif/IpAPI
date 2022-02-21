# Django
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Myserializer
import requests
from . requestapi import get_location


@api_view(['GET'])
def location_detail(request):                                
    serializer = Myserializer(data=request.GET)          
    serializer.is_valid()                                  
    query = serializer.validated_data['query']
    ip_info = get_location(query) 
    return Response(ip_info)


