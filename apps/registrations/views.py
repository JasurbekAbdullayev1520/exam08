from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


from .models import Registration
from .serializers import RegistrationSerializer
from apps.events.models import Event

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Registration.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        event = Event.objects.get(pk=pk)
        user = request.user
        if event.capacity == 0:
            return Response({'error': 'Event is full.'}, status=status.HTTP_400_BAD_REQUEST)
        
        count = Registration.objects.filter(event=event).count()
        if count >= event.capacity:
            return Response({'error': 'Event is full.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Registration.objects.filter(event=event, user=user).exists():
            return Response({'error': 'You are already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)
        
        Registration.objects.create(user=user, event=event)
        return Response({'message': 'Successfully registered for this event.'}, status=status.HTTP_201_CREATED)
        