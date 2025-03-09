from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your models here.

class Article(models.Model):

    def get_default_user():
        return get_user_model().objects.first().id

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=get_default_user)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50] + '...'

