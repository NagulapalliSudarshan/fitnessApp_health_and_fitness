from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('posts-detail',kwargs={"pk":self.pk})

    def __str__(self):
        return self.title

# Create your models here.
