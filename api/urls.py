
from django.urls import path
from  api import views


urlpatterns = [
    path(
        route = 'api', #/api?query=24.10.0.1
        view = views.location_detail,
    )
   
]
