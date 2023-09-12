from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class PeopleAPIView(ModelViewSet):
     queryset = People.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = PeopleSerializer #informa o serializer
     
class PlanetAPIView(ModelViewSet):
     queryset = Planet.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = PlanetSerializer #informa o serializer   

class StarshipAPIView(ModelViewSet):
     queryset = Starships.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = StarshipsSerializer #informa o serializer   