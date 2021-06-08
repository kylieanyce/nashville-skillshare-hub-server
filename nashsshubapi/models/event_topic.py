from django.db import models
from django.db.models.deletion import CASCADE



class EventTopic(models.Model):
    topic = models.ForeignKey("Topic", on_delete=CASCADE)
    event = models.ForeignKey("Event", on_delete=CASCADE)