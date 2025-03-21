from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .api import HotelViewsets
 

app_name = "hotel"

router = DefaultRouter()
router.register('', HotelViewsets)

urlpatterns = [
    path('', include(router.urls)),
]