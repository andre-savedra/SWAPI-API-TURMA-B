from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class PeopleAPIView(APIView):
    def get(self, request, peopleId = ''):
        #se o get não tiver o filtro de id:
        if peopleId == '':   
            #seleciona tudo!     
            peopleFound = People.objects.all() #select *from people; #PYTHON
            serializer = PeopleSerializer(peopleFound, many=True) #JSON
            return Response(serializer.data) #devolvendo ao cliente o JSON!
        #busca por people id:
        peopleFound = People.objects.get(id=peopleId) #select *from people where id = peopleId 
        serializer = PeopleSerializer(peopleFound, many=False) #JSON
        return Response(serializer.data)
        
class PlanetAPIView(APIView):
    def get(self, request):
        planetFound = Planet.objects.all() #select *from planet; #PYTHON
        serializer = PlanetSerializer(planetFound, many=True) #JSON
        return Response(serializer.data) #devolvendo ao cliente o JSON!


class StarshipAPIView(APIView):
    def get(self, request):
        starshipFound = Starships.objects.all() #select *from Starship; #PYTHON
        serializer = StarshipsSerializer(starshipFound, many=True) #JSON
        return Response(serializer.data) #devolvendo ao cliente o JSON!