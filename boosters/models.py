from uuid import uuid4
from django.db import models

class Booster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=36)
    common_probability = models.DecimalField(max_digits=5, decimal_places=2)
    rare_probability = models.DecimalField(max_digits=5, decimal_places=2)
    epic_probability = models.DecimalField(max_digits=5, decimal_places=2)
    legendary_probability = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.IntegerField()