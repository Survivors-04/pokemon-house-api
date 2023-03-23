from uuid import uuid4
from django.db import models

from utils.pokemons.choices import RARITY_CHOICES, TYPE_CHOICES

class Pokemons(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=36)
    rarity = models.CharField(max_length=36, choices=RARITY_CHOICES)
    number = models.IntegerField()
    type01 = models.CharField(max_length=36, choices=TYPE_CHOICES)
    type02 = models.CharField(max_length=36, null=True, choices=TYPE_CHOICES)
    # userId = models.CharField(max_length=36)
    price = models.IntegerField(default=0)
