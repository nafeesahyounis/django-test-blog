from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    
    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=500, blank=False)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ForeignKey(Tags, null=True, blank=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()



   

