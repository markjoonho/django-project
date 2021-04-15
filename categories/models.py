from django.db import models
from core import models as core_models


class Category(core_models.TimeStampedModel):

    """ Category Model Definition """

    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"

    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "Both"),
    )

    name = models.CharField(max_length=20, default="")
    kind = models.CharField(choices=KIND_CHOICES, max_length=5, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
