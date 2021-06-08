from django.db import models

class Topic(models.Model):
    label = models.CharField(max_length=50)