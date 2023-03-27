from decimal import Decimal
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
    name = models.CharField(max_length=36, unique=True)
    rarity = models.CharField(max_length=36, choices=RARITY_CHOICES)
    pokedex = models.IntegerField()
    type_1 = models.CharField(max_length=36, choices=TYPE_CHOICES)
    type_2 = models.CharField(max_length=36, null=True, choices=TYPE_CHOICES)

class PokemonUser(Pokemons):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pokemons')
    price = models.IntegerField(default=0)

class PokemonBooster(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=36)
    common_probability = models.DecimalField(max_digits=5, decimal_places=2)
    rare_probability = models.DecimalField(max_digits=5, decimal_places=2)
    epic_probability = models.DecimalField(max_digits=5, decimal_places=2)
    legendary_probability = models.DecimalField(max_digits=5, decimal_places=2)
