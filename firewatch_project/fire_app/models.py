from django.db import models

class FireData(models.Model):
    month = models.CharField(max_length=4)
    day = models.CharField(max_length=4)
    temp = models.FloatField()
    relative_humidity = models.FloatField()
    wind = models.FloatField()
    rain = models.FloatField()
    area = models.FloatField()

    def __str__(self):
        return self.month + " " + self.day


