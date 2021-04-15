from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Defintion"""

    list_display = (
        "text",
        "rating",
        "created_by",
        "movie",
        "book",
    )

    list_filter = (
        "rating",
        "created_by",
        "movie",
        "book",
    )
