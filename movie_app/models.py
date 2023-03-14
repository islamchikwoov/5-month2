from django.db import models
# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name




class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    directors = models.ForeignKey(Director, null=True, blank=True, on_delete=models.CASCADE,
                                  related_name='movie_count')

    def __str__(self):
        return self.title





STARS = (
        (1, '*'),
        (2, 2 * '* '),
        (3, 3 * '* '),
        (4, 4 * '* '),
        (5, 5 * '* '),
    )

class Reviews(models.Model):
    text = models.TextField(null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
            related_name='movie_reviews')
    stars = models.IntegerField(choices=STARS, default=1)

    def __str__(self):
        return self.text










