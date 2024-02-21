from typing import Any
from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    # * Notes fields
    title = models.CharField(max_length=200)
    text = models.TextField()
    # "auto_now_add" Current date
    created = models.DateTimeField(auto_now_add=True)
    # "on_delete" If a user is delete his notes will also.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")