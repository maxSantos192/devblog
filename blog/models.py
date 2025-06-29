from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=15)

class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True)

class Post(models.Model):
    title = models.CharField(max_length=100)
    legend = models.CharField(max_length=200)
    image = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    read_time = models.IntegerField(default=0)
    content = models.TextField()
    tags = models.CharField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_image = models.URLField(blank=True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)