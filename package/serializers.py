from rest_framework import serializers
from.models import Umrah,Hajj

class UmrahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Umrah
        fields = '__all__'


class HajjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hajj
        fields = '__all__'