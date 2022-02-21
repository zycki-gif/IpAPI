
from django.urls import path
from  api import views


urlpatterns = [
    path(
        route = 'api', # /weather?city=$City&country=$Country&
        view = views.location_detail,
    )
   
]