from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
