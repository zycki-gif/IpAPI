
from django.urls import path
from  api import views


urlpatterns = [
    path(
        route = 'api', 
        view = views.location_detail,
    )
   
]
