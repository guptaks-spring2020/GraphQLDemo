from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.TextField(blank=True)
    url = models.URLField()