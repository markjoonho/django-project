from django.contrib import admin
from . import models


@admin.register(models.Favourite)
class FavouriteAdmin(admin.ModelAdmin):

    """ FavouriteAdmin Defintion """

    pass
