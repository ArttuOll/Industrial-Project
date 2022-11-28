from rest_framework.serializers import ModelSerializer

from .models import Patient

class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'patient_id'
        )