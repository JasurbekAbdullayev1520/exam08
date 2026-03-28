from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'
        
    def validate(self, data):
        model = Registration
        fields = '__all__'
        read_only_fields = ('user', 'status',)
        
        