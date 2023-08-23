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
        try:
            peopleFound = People.objects.get(id=peopleId) #select *from people where id = peopleId 
            serializer = PeopleSerializer(peopleFound, many=False) #JSON
            return Response(serializer.data)
        except People.DoesNotExist:
            return Response(status=404,  data="People not Found!!!!")
    
    def post(self, request):
        #pega o Json do cliente e guardando na variavel
        peopleJson = request.data
        #convertendo o JSON em Python!!!!
        peopleSerialized = PeopleSerializer(data=peopleJson, many=False) 
        #verificar se os dados estão coerentes!!!!
        if peopleSerialized.is_valid():
            #salvando no banco de dados!!!!
            peopleSerialized.save()
            return Response(status=203, data=peopleSerialized.data)
        return Response(status=400, data="Mande certo seu imbecil!")



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