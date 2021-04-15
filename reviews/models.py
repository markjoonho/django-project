from django.db import models
from movies import models as movie_models
from core import models as core_models
from books import models as book_models
from users import models as user_models

# Create your models here.


class Review(core_models.TimeStampedModel):

    """ Review Model Definiton """

    created_by = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    text = models.TextField()
    movie = models.ForeignKey(
        movie_models.Movie, on_delete=models.CASCADE, null=True, blank=True
    )
    book = models.ForeignKey(
        book_models.Book, on_delete=models.CASCADE, null=True, blank=True
    )
    rating = models.IntegerField()

    def __str__(self):
        result = self.text
        if self.book is not None:
            result = result + " - " + f"{self.book}"
        if self.movie is not None:
            result = result + " - " + f"{self.movie}"

        return result
