from django.db import models

class Location(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    countryCode = models.CharField(max_length=5)
    timeZone = models.CharField(max_length=50, blank=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    seq = models.PositiveSmallIntegerField(null=True)
    visible = models.BooleanField(default=True)

    class Meta:
        db_table = "location"

    def __str__(self):
        return self.city
