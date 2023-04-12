from rest_framework import serializers
from .models import RatingChoices


class MovieSerializer:
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, required=False)
    ratings = serializers.ChoiceField(
        max_length=20, choices=RatingChoices.choices, required=False
    )
    synopsis = serializers.TextField(required=False)
