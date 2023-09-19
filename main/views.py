from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated

class PeopleAPIView(ModelViewSet):
     queryset = People.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = PeopleSerializer #informa o serializer
     filter_backends = [DjangoFilterBackend] #usa a lib django-filter
     filterset_fields = ['name', 'eyeColor', 'height', 'gender']
     permission_classes = (IsAuthenticated,)  

        
class PlanetAPIView(ModelViewSet):
     queryset = Planet.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = PlanetSerializer #informa o serializer   
     filter_backends = [DjangoFilterBackend] #usa a lib django-filter
     filterset_fields = ['name', 'diameter']
     permission_classes = (IsAuthenticated,)       

class StarshipAPIView(ModelViewSet):
     queryset = Starships.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = StarshipsSerializer #informa o serializer   
     filter_backends = [DjangoFilterBackend] #usa a lib django-filter
     filterset_fields = ['name', 'model', 'passengers']
     permission_classes = (IsAuthenticated,)  