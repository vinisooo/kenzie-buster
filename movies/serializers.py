from rest_framework import serializers
from rest_framework.response import Response
from .models import RatingChoices
from .models import Movie, MovieOrder
from datetime import datetime
from users.models import User


class MovieSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices, default="G", required=False
    )
    synopsis = serializers.CharField(required=False)
    added_by = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)

    def get_added_by(self, obj):
        user = User.objects.get(id=obj.user_id)
        return user.email


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.SerializerMethodField(read_only=True)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2, required=True)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)

    def get_buyed_by(self, obj):
        buyer = User.objects.get(id=obj.user_id)
        return buyer.email

    def get_title(self, obj):
        try:
            movie = Movie.objects.get(id=obj.movie_id)
        except Movie.DoesNotExist:
            return Response({"detail": "Movie not found"}, 404)
        return movie.title
