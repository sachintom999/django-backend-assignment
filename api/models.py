from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """A description of the Post model"""

    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
