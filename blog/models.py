from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    content = models.TextField()
    category = models.ForeignKey(Category, blank=True, null=True)
    cre_date = models.DateTimeField()
    update = models.DateTimeField()

    def __str__(self):
        return self.title
