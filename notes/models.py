from typing import Any
from django.db import models

class Notes(models.Model):
    # * Notes fields
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)