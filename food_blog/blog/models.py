import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    image = models.ImageField(upload_to="uploads/", null=True, blank=True)
    likes = models.IntegerField(default=0)
    date_posted = models.DateTimeField("date published")
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.date_posted >= timezone.now() - datetime.timedelta(days=1)
