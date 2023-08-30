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


# urlpatterns = [
#     path('people',PeopleAPIView, name="people"),
#     # path('people/<int:peopleId>',PeopleAPIView.as_view(), name="peopleById"),
#     path('planet/',PlanetAPIView.as_view(), name="planet"),
#     path('starship/',StarshipAPIView.as_view(), name="starship"),
# ]


