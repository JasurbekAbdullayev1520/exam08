from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Count, Q

from apps.events.models import Event
from apps.registrations.models import Registration

class EventStatsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        events = Event.objects.all()
        
        data =[]
        for event in events:
            registrated_count = Registration.objects.filter(event=event, status='REGISTERED').count()
             
            available_slots = event.capacity - registrated_count 
            
            data.append({
                'event_id': event.id,
                'title': event.title,
                'registration_count': registrated_count,
                'available_slots': available_slots,
            })
            
            return Response(data)
        