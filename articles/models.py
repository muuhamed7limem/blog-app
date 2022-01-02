from django.db import models
from django.db.models import Model
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Article(Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=600)
    slug = models.SlugField(max_length=70)
    date = models.DateField(auto_now_add=True)
    thumb = models.ImageField(upload_to='staticfiles/')
    author = models.ForeignKey(User, default=None, on_delete=CASCADE)

    def __str__(self):
        return self.slug