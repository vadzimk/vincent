from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body = models.TextField()

    # should add a get_absolute_url() and __str__() method to each model you write.
    def __str__(self):
        return self.title

    def get_absolute_url(self):  # sets the method url on the form tag
        return reverse('post_detail', args=[str(self.id)])
