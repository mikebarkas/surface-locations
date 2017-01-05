from django.db import models


class LocationManager(models.Manager):

    def cities_by_state(self, state):
        return self.get_queryset().filter(state=state.upper()).order_by('city').distinct('city')

    def city(self, state, city):
        return self.get_queryset().filter(state=state.upper(), city=city.upper())


class Location(models.Model):

    city = models.CharField(max_length=200)
    state = models.CharField(max_length=5)
    zipcode = models.CharField(max_length=15)
    population = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.city

    objects = LocationManager()
