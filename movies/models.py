import datetime
from django.db import models
from categories import models as category_models
from core import models as core_models
from people import models as people_models

YEAR_CHOICES = []
for r in range(1800, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))


class Movie(core_models.TimeStampedModel):

    """ Movie Model Definition """

    title = models.CharField(max_length=100)
    year = models.IntegerField(
        ("year"),
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
    )
    cover_image = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField(category_models.Category, blank=True)
    rating = models.IntegerField()
    director = models.ForeignKey(
        people_models.Person, on_delete=models.CASCADE, related_name="director"
    )
    cast = models.ManyToManyField(people_models.Person, blank=True, related_name="cast")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
