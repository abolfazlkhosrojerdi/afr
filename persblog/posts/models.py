from django.db import models


class Post(models.Model):
    title  = models.CharField(max_length=50)
    author = ''
    is_enable = models.BooleanField(default=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    text = models.TextField(blank=True)

# Create your models here.
