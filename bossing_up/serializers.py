from rest_framework.serializers import ModelSerializer
from .models import BlackBusiness

class BlackBusinessSerializer(ModelSerializer):
    class Meta:
        model = BlackBusiness
        fields = '__all__'

class BlackBusinessDetailSerializer(ModelSerializer):
    class Meta:
        model = BlackBusiness
        fields = '__all__'