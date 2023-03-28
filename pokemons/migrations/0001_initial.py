# Generated by Django 4.1.7 on 2023-03-28 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PokemonBooster",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=36)),
                (
                    "common_probability",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "rare_probability",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "epic_probability",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
                (
                    "legendary_probability",
                    models.DecimalField(decimal_places=2, max_digits=5),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pokemons",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=36)),
                (
                    "rarity",
                    models.CharField(
                        choices=[
                            ("C", "common"),
                            ("R", "rare"),
                            ("E", "epic"),
                            ("L", "legendary"),
                        ],
                        max_length=36,
                    ),
                ),
                ("pokedex", models.IntegerField()),
                (
                    "type_1",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=36,
                    ),
                ),
                (
                    "type_2",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=36,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PokemonUser",
            fields=[
                (
                    "pokemons_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="pokemons.pokemons",
                    ),
                ),
                ("price", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pokemons",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("pokemons.pokemons",),
        ),
    ]
