import datetime

from django.db import models
from django.utils import timezone

class User(models.Model):
    user_name =models.CharField(max_length=32)
    password = models.CharField(max_length=20)
    email =  models.EmailField()

    def __str__(self):
        return self.user_name 


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    ##image =
    likes = models.IntegerField(default=0)
    date_posted = models.DateTimeField("date published")
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)
