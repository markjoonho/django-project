from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "writer",
        "rating",
    )

    list_filter = (
        "title",
        "writer",
        "rating",
        "year",
    )
