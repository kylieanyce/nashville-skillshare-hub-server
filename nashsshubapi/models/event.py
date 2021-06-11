from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import related


class Event(models.Model):
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    cost = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    description = models.TextField()
    hostname = models.CharField(max_length=100)
    hosts = models.ManyToManyField(User, through="Host", related_name="events")
    topics = models.ManyToManyField(
        "Topic", through="EventTopic", related_name="events")
    bookmarks = models.ManyToManyField(
        User, through="Bookmark", related_name="bookmarks")

    @property
    def bookmarked(self):
        return self.__bookmarked

    @bookmarked.setter
    def bookmarked(self, value):
        self.__bookmarked = value
