from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    gold = models.IntegerField(default=100)
    dateRoll = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
