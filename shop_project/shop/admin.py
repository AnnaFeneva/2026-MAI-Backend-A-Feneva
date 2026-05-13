from django.contrib import admin
from .models import Game, Genre, Platform, Profile, Favorite, Review

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Platform)
admin.site.register(Profile)
admin.site.register(Favorite)
admin.site.register(Review)