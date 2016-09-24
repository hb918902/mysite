from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = {
    0:u'草稿',
    1:u'发布',
    2:u'删除',
}

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
    cre_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=0,choices=STATUS.items())

    def __str__(self):
        return self.title
