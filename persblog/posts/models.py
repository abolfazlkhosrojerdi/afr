from django.db import models


class Post(models.Model):
    title  = models.CharField(max_length=50)
    author = ''
    is_enable = models.BooleanField(default=True)
    publish_date = models.DateTimeField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    text = models.TextField()

# Create your models here.
