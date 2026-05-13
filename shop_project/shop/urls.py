from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile),

    path('games/', views.get_games),
    path('games/create/', views.create_game),
    path('games/delete/<int:id>/', views.delete_game),

    path('search/', views.search),
    path('genres/', views.genre),
    path('platforms/', views.platforms),

    path('', views.web_index),

    # DRF endpoints

    path('drf/games/', views.GameListCreateView.as_view()),
    path('drf/games/<int:pk>/', views.GameDetailView.as_view()),

    path('drf/genres/', views.GenreListCreateView.as_view()),
    path('drf/genres/<int:pk>/', views.GenreDetailView.as_view()),

    path('drf/platforms/', views.PlatformListCreateView.as_view()),
    path('drf/platforms/<int:pk>/', views.PlatformDetailView.as_view()),

    path('drf/reviews/', views.ReviewListCreateView.as_view()),
    path('drf/reviews/<int:pk>/', views.ReviewDetailView.as_view()),
]