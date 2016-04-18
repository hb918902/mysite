from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    content = models.TextField()
    tags = models.CharField(max_length=30,blank=True)
    cre_date = models.DateTimeField()
    update = models.DateTimeField()

    def __str__(self):
        return self.title
