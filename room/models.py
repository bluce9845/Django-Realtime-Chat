from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)
    
class Message(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)