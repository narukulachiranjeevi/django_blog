from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique_for_date='published',max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    body = models.TextField()
    publish= models.DateField(default=timezone.now())
    updated = models.DateField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering= ('-publish' ,) 

    def __str__(self):
        return self.title

















