from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from django.contrib.gis.db import models
import datetime

# Create your models here.

class Post (models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    text=models.TextField(max_length=100,default=None)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        app_label = 'user'

        def __str__(self):
            return self.name  
