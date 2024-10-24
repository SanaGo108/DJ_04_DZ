from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.title

