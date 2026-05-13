from django.db import models
from django.contrib.auth.models import User

# OneToOne
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)


# Genre (бывший Category)
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Platform (НОВАЯ МОДЕЛЬ)
class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Game (бывший Product)
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    platform = models.ManyToManyField(Platform, blank=True)

    def __str__(self):
        return self.title


# Review (НОВАЯ)
class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
    ])


# ManyToMany (избранное)
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Game)