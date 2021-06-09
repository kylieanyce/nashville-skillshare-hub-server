from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


class Host(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    event = models.ForeignKey("Event", on_delete=CASCADE)
    name = models.CharField(max_length=100)
