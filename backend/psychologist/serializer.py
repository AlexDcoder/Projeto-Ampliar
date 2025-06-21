from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Psychologist

class PsychologistSerializer(ModelSerializer):
    class Meta:
        model = Psychologist
        fields = '__all__'
        read_only_fields = ['id']
    
    def validate_crp(self, value):
        if self.instance:
            if Psychologist.objects.exclude(id=self.instance.id).filter(crp=value).exists():
                raise ValidationError("This CRP is already registered.")
        if Psychologist.objects.filter(crp=value).exists():
            raise ValidationError("This CRP is already registered.")
        return value