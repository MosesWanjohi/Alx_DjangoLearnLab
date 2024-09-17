
from .models import CustomUser
from rest_framework import serializers

#Creating Custom User Serializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

