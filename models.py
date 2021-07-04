from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title=models.CharField(max_length=100, null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return self.title

    class Meta:
        ordering=['complete']

