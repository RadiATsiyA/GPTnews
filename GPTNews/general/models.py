from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField(max_length=3500)
    date = models.DateField(auto_now_add=True)
    img_big = models.ImageField(upload_to='article_images_big')
    img_small = models.ImageField(upload_to='article_images_small')
