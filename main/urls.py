#biblioteca p/ trabalhar com as rotas/endpoints
from django.urls import path

#importando tudo o que tem nas nossas views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PeopleAPIView)
router.register(r'planet', PlanetAPIView)
router.register(r'starship', StarshipAPIView)

urlpatterns = router.urls

