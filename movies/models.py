from django.db import models


class RatingChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, blank=True)
    rating = models.CharField(
        max_length=20, choices=RatingChoices.choices, default=RatingChoices.G
    )
    synopsis = models.TextField(blank=True, null=True)


class MovieOrder(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    buyed_at = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
