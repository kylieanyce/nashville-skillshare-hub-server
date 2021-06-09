from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related


class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    cost = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    hosts = models.ManyToManyField(User, through="Host", related_name="events")
    topics = models.ManyToManyField("Topic", through="EventTopic", related_name="events")
    bookmarks = models.ManyToManyField(User, through="Bookmark", related_name="bookmarks")