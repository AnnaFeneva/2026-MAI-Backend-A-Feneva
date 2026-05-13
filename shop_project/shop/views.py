from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .models import Game, Genre, Platform, Review
from rest_framework import generics
from .serializers import GameSerializer, GenreSerializer, PlatformSerializer, ReviewSerializer
import json

@require_http_methods(["GET"])
def profile(request):
    return JsonResponse({
        "user": "test_user",
        "favorites": []
    })

@require_http_methods(["GET"])
def products(request):
    return JsonResponse({
        "products": []
    })

@require_http_methods(["GET"])
def genre(request):
    data = list(Genre.objects.values("id", "name"))
    return JsonResponse({"genres": data}, json_dumps_params={"indent":4})

@require_http_methods(["GET"])
def platforms(request):
    data = list(Platform.objects.values("id", "name"))
    return JsonResponse({"platforms": data}, json_dumps_params={"indent":4})


@csrf_exempt
@require_http_methods(["POST"])
def add_to_favorites(request):
    return JsonResponse({
        "status": "ok"
    })

@require_http_methods(["GET"])
def search(request):
    query = request.GET.get("q", "")

    games = Game.objects.filter(
        Q(title__icontains=query) | Q(description__icontains=query)
    )

    data = []
    for g in games:
        data.append({
            "id": g.id,
            "title": g.title,
            "description": g.description
        })

    return JsonResponse({"results": data}, json_dumps_params={"indent": 4})

@require_http_methods(["GET"])
def get_games(request):
    games = Game.objects.all()

    data = []
    for g in games:
        data.append({
            "id": g.id,
            "title": g.title,
            "description": g.description,
            "price": str(g.price),
            "genre": g.genre.name,
            "platform": ", ".join([p.name for p in g.platform.all()])
        })

    return JsonResponse({"games": data}, json_dumps_params={"indent": 4})

@csrf_exempt
@require_http_methods(["POST"])
def create_game(request):
    body = json.loads(request.body)

    game = Game.objects.create(
        title=body.get("title"),
        description=body.get("description"),
        price=body.get("price"),
        genre_id=body.get("genre_id"),
        platform_id=body.get("platform_id")
    )

    return JsonResponse({
        "status": "created",
        "id": game.id
    })

@csrf_exempt
@require_http_methods(["POST"])
def delete_game(request, id):
    game = Game.objects.get(id=id)
    game.delete()

    return JsonResponse({
        "status": "deleted",
        "id": id
    })


class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlatformListCreateView(generics.ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class PlatformDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

from django.http import HttpResponse

def web_index(request):
    return HttpResponse("<h1>Главная страница</h1>")