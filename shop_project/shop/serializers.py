from rest_framework import serializers
from .models import Game, Genre, Platform, Review


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class GameSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    platform = serializers.PrimaryKeyRelatedField(
        queryset=Platform.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Game
        fields = '__all__'

    def create(self, validated_data):
        platforms = validated_data.pop('platform', [])
        game = Game.objects.create(**validated_data)
        game.platform.set(platforms)
        return game


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'