from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

class PeopleAPIView(viewsets.ModelViewSet):
        queryset = People.objects.all()
        serializer_class = PeopleSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['name', 'eyeColor']

class PlanetAPIView(viewsets.ModelViewSet):
        queryset = Planet.objects.all()
        serializer_class = PlanetSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['name', 'climate', 'diameter']


class StarshipAPIView(viewsets.ModelViewSet):
        queryset = Starships.objects.all()
        serializer_class = StarshipsSerializer
        filter_backends = [DjangoFilterBackend]
        filterset_fields = ['name', 'model', 'passengers']