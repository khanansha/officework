from rest_framework import serializers
from .models import SavedEmbeds,Registration

class EmbedSerializer(serializers.ModelSerializer):
    class Meta:
        model =Registration 
      


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registration
        fields='__all__'