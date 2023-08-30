from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class PeopleAPIView(APIView):
    def get(self, request, peopleId = ''):
        #se o get não tiver o filtro de id:
        if peopleId == '':   
            peopleFound = ''
            #se passarem o filtro de 'name'
            if 'name' in request.GET and 'eyeColor' in request.GET:
                nameToFilter = request.GET['name']
                eyeToFilter = request.GET['eyeColor']
                peopleFound = People.objects.filter(name__contains=nameToFilter).filter(eyeColor__contains=eyeToFilter)                
            elif 'name' in request.GET:
                #pegando o parâmetro que foi informado!
                nameToFilter = request.GET['name']
                #SELECT *FROM PEOPLE WHERE NAME LIKE %nameToFilter%;
                peopleFound = People.objects.filter(name__contains=nameToFilter)
            elif 'eyeColor' in request.GET:
                eyeToFilter = request.GET['eyeColor']
                peopleFound = People.objects.filter(eyeColor__contains=eyeToFilter)    
            else:
                #seleciona tudo!     
                peopleFound = People.objects.all() #select *from people; #PYTHON
            serializer = PeopleSerializer(peopleFound, many=True) #JSON
            return Response(status=200, data=serializer.data) #devolvendo ao cliente o JSON!
        #busca por people id:
        try:
            peopleFound = People.objects.get(id=peopleId) #select *from people where id = peopleId 
            serializer = PeopleSerializer(peopleFound, many=False) #JSON
            return Response(status=200,data=serializer.data)
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
    
    def delete(self, request, peopleId = ''):

        if(peopleId != ''):
            #procurar a pessoa com o Id!
            peopleFound = People.objects.get(id=peopleId)
            #deletando o usuario encontrado!
            peopleFound.delete()
            return Response(status=200, data='People successfully deleted!')

        #cliente da API não passou o peopleId para deletar!
        return Response(status=400, data='PeopleId must be given!') 

    def put(self, request, peopleId = ''):  
         
         if(peopleId != ''):
             #procurar o antigo no banco:
             peopleFound = People.objects.get(id=peopleId)

             #coletar o novo que veio JSON:
             peopleToUpdateJSON = request.data
             
             #faz o serializer substituir o novo pelo antigo e converter em python
             serializedPeople = PeopleSerializer(peopleFound, data=peopleToUpdateJSON)

             #verificar se a conversão é válida
             if(serializedPeople.is_valid()):
                 #salvo no banco de dadps
                 serializedPeople.save()
                 return Response(status=200, data=serializedPeople.data)
             return Response(status=400, data='Invalid Data!')
             
         #cliente da API não passou o peopleId para editar!
         return Response(status=400, data='PeopleId must be given!') 


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