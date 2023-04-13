from django.urls import path
from .views import MovieView, MovieDetailView, MovieOrderDetailView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailView.as_view()),
    path("movies/<int:movie_id>/order/", MovieOrderDetailView.as_view()),
]
