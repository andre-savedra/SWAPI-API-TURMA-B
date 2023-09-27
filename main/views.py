from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import django_filters


#crio um filter personalizado para o People fazendo com que busque os nomes com o LIKE no banco de dados
# e também as alturas que sejam maiores ou iguais ao que especificar
class PeopleFilter(django_filters.FilterSet):
     name = django_filters.CharFilter(lookup_expr='icontains')
     height = django_filters.NumberFilter(lookup_expr='gte')

     class Meta:
          model = People
          fields = ['name', 'height']


class PeopleAPIView(ModelViewSet):
     queryset = People.objects.all() #informa p/ a lib qual as consultas a serem feitas
     serializer_class = PeopleSerializer #informa o serializer
     filter_backends = [DjangoFilterBackend] #usa a lib django-filter
     filterset_class = PeopleFilter #registra o filtro customizado

        
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