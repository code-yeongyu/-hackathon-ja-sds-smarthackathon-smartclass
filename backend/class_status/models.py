from django.db import models

from imagekit.models import ImageSpecField


class Status(models.Model):
    arduino_id = models.IntegerField(null=False, default=-1)
    image = models.ImageField(upload_to='./detect/%Y%m%d/', )
    gas_quality = models.FloatField(null=False)
    air_quality = models.FloatField(null=False)