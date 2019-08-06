from django.db import models
from django.conf import settings


class Class(models.Model):
    className = models.CharField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    student_id = models.CharField(
        max_length=50, null=True)  # student id from school id barcode
    class_id = models.CharField(max_length=50)  # the id of arduino
    bio = models.CharField(max_length=50)
