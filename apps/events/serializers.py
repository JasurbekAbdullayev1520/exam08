from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        
    def validate(self, data):
        if data['end_time'] <= data['start_time']:
            raise serializers.ValidationError('End time must be after start time.')
        return data
    