from django.db import models

from imagekit.models import ImageSpecField


class Image(models.Model):
    image = models.ImageField(upload_to='static/uploaded/images/%Y/%m/%d/', )
    arduino_id = models.IntegerField(null=False, default=-1)