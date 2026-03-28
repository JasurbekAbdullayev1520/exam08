from django.db import models
from django.conf import settings


class Event(models.Model):
    EVENT_TYPES = (
        ('ONLINE', 'Online'),
        ('OFFLINE', 'Offline'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    event_type = models.CharField(max_length=10, choices=EVENT_TYPES)
    date = models.DateTimeField()
    location = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    def clean(self):
        if self.event_type == 'OFFLINE' and not self.location:
            raise ValidationError('Location is required for offline events.')
        if self.start_time >= self.end_time:
            raise ValidationError('Start time must be before end time.')
    
    def __str__(self):
        return self.title
    

    
    
