from django.db import models
from core import models as core_models
from books import models as book_models
from movies import models as movie_models
from users import models as user_models


class Favourite(core_models.TimeStampedModel):

    """ Fav Model Definition """

    created_by = models.OneToOneField(user_models.User, on_delete=models.CASCADE)

    books = models.ManyToManyField(book_models.Book, blank=True)
    movies = models.ManyToManyField(movie_models.Movie, blank=True)

    def __str__(self):
        return f"{self.created_by}'s favourite list"
