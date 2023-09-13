from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class PeopleAPIView(ModelViewSet):
     queryset = People.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = PeopleSerializer #informa o serializer
     filter_backends = [DjangoFilterBackend] #usa a lib django-filter
     filterset_fields = ['name', 'eyeColor', 'height', 'gender']
        
class PlanetAPIView(ModelViewSet):
     queryset = Planet.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = PlanetSerializer #informa o serializer   
     filter_backends = [DjangoFilterBackend] #usa a lib django-filter
     filterset_fields = ['name', 'diameter']

class StarshipAPIView(ModelViewSet):
     queryset = Starships.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = StarshipsSerializer #informa o serializer   
     filter_backends = [DjangoFilterBackend] #usa a lib django-filter
     filterset_fields = ['name', 'model', 'passengers']