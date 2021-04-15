from django.contrib import admin
from . import models


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "director",
        "rating",
    )

    list_filter = (
        "title",
        "director",
        "rating",
        "year",
    )
