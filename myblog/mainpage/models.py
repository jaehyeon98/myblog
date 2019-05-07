from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=False)
    body = models.TextField()
    def __str__(self):
        return self.title

# Create your models here.
