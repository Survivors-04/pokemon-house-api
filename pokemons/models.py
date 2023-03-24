from uuid import uuid4
from django.db import models

from users.models import User

TYPE_CHOICES = (
    ("normal", "normal"),
    ("fire", "fire"),
    ("water", "water"),
    ("grass", "grass"),
    ("electric", "electric"),
    ("ice", "ice"),
    ("fighting", "fighting"),
    ("poison", "poison"),
    ("ground", "ground"),
    ("flying", "flying"),
    ("psychic", "psychic"),
    ("bug", "bug"),
    ("rock", "rock"),
    ("ghost", "ghost"),
    ("dark", "dark"),
    ("dragon", "dragon"),
    ("steel", "steel"),
    ("fairy", "fairy"),
)

RARITY_CHOICES = (
    ("C", "common"),
    ("R", "rare"),
    ("E", "epic"),
    ("L", "legendary"),
)


class Pokemons(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=36)
    rarity = models.CharField(max_length=36, choices=RARITY_CHOICES)
    number = models.IntegerField()
    type01 = models.CharField(max_length=36, choices=TYPE_CHOICES)
    type02 = models.CharField(max_length=36, null=True, choices=TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pokemons')
    price = models.IntegerField(default=0)
