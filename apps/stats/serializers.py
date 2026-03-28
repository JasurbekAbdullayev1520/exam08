from rest_fremfork import serializers

class EventStatsSerializer(serializers.Serializer):
    event_id = serializers.IntegerField()
    title = serializers.CharField()
    registration_count = serializers.IntegerField()
    available_slots = serializers.IntegerField()
    
    
    
    
    