from rest_framework import viewsets
from.models import Hajj,Umrah
from.serializers import UmrahSerializer,HajjSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UmrahViewsets(viewsets.ModelViewSet):
    queryset = Umrah.objects.all()
    serializer_class = UmrahSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class HajjViewsets(viewsets.ModelViewSet):
    queryset = Hajj.objects.all()
    serializer_class = HajjSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]