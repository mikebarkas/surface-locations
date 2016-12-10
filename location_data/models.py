from django.db import models


class Location(models.Model):

    city = models.CharField(max_length=200)
    state = models.Charfield(max_length=5)
    zipcode = models.PositiveIntegerField()
    population = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.city
