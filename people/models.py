from django.db import models
from core import models as core_models


class Person(core_models.TimeStampedModel):

    """ Person Model Definition """

    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"

    KIND_CHOICES = (
        (KIND_ACTOR, "Actor"),
        (KIND_DIRECTOR, "Director"),
        (KIND_WRITER, "Writer"),
    )

    name = models.CharField(max_length=20, default="")
    kind = models.CharField(choices=KIND_CHOICES, max_length=8, default="")
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "People"
