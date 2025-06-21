from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Psychologist

class PsychologistSerializer(ModelSerializer):
    class Meta:
        model = Psychologist
        fields = '__all__'
        read_only_fields = ['id']