from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import MovieSerializer, MovieOrderSerializer
from .models import Movie, MovieOrder
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import MoviesPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, MoviesPermission]

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, 201)

    def get(self, request):
        movies = Movie.objects.all()

        page_result = self.paginate_queryset(movies, request, view=self)
        serializer = MovieSerializer(page_result, many=True)
        return self.get_paginated_response(serializer.data)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, MoviesPermission]

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id).delete()
        except Movie.DoesNotExist:
            return Response({"detail": "Movie not found"}, 404)

        return Response(movie, 204)

    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Movie not found"}, 404)

        serializer = MovieSerializer(movie, many=False)

        return Response(serializer.data, 200)


class MovieOrderDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

    def post(self, request, movie_id):
        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie_id=movie_id, user_id=request.user.id)

        return Response(serializer.data, 201)
