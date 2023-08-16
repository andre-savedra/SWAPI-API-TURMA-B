#biblioteca p/ trabalhar com as rotas/endpoints
from django.urls import path

#importando tudo o que tem nas nossas views
from .views import *

urlpatterns = [
    path('people/',PeopleAPIView.as_view(), name="people"),
    path('people/<int:peopleId>',PeopleAPIView.as_view(), name="peopleById"),
    path('planet/',PlanetAPIView.as_view(), name="planet"),
    path('starship/',StarshipAPIView.as_view(), name="starship"),
]


