from django.db import models


# Create your models here.
class Article(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey('auth.user',
                               related_name='article',
                               on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=True)

    class Meta:
        ordering = ('created_at', )