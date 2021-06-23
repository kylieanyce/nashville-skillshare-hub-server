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

    # sets a new property onto Event object called 'bookmarked' that
    # changes between true and false to determine if more custom
    # action must be taken, ie: looking at the bookmarks property
    @property
    def bookmarked(self):
        return self.__bookmarked

    @bookmarked.setter
    def bookmarked(self, value):
        self.__bookmarked = value

    # same as above but with organizers/hosts
    @property
    def organizers(self):
        return self.__organizers

    @organizers.setter
    def organizers(self, value):
        self.__organizers = value
