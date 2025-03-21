from rest_framework import viewsets
from.models import Hotel
from.serializers import HotelSerializer

class HotelViewsets(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer