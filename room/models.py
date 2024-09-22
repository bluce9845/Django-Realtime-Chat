from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(unique=True)