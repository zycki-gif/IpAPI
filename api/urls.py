
from django.urls import path
from  api import views


urlpatterns = [
    path(
        route = 'api', #/api?query=
        view = views.location_detail,
    )
   
]
