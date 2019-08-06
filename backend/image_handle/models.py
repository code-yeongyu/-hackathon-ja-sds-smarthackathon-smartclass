from django.db import models

from imagekit.models import ImageSpecField


class Image(models.Model):
    image = models.ImageField(upload_to='./detect/%Y%m%d/', )
    arduino_id = models.IntegerField(null=False, default=-1)