from django.db import models
from django.conf import settings
from apps.events.models import Event

class Registration(models.Model):
    STATUS = (
        ('REGISTERED', 'Registered'),
        ('CANCELLED', 'Cancelled'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='REGISTERED')
    created_at = models.DateTimeField(auto_now_add=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('event', 'user')
    
    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"
