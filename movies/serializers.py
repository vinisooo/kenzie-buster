from rest_framework import serializers
from .models import RatingChoices
from .models import Movie
from datetime import datetime


class MovieSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices, default="G", required=False
    )
    synopsis = serializers.CharField(required=False)

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(read_only=True, source="movie.title")
    buyed_by = serializers.EmailField(read_only=True, source="user.email")
    buyed_at = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def get_buyed_at(self, obj):
        now = datetime.now()
        current_date = now.strftime()
        return current_date
