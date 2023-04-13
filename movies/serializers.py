from rest_framework import serializers
from .models import RatingChoices
from .models import Movie


class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    rating = serializers.ChoiceField(
        choices=RatingChoices.choices, default="G", required=False
    )
    synopsis = serializers.CharField(required=False)

    def create(self, validated_data: dict):
        return Movie.objects.create(**validated_data)
