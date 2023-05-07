from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField(max_length=3500)
    date = models.DateField(auto_now_add=True)
    img_big = models.ImageField(upload_to='article_images_big')
    img_small = models.ImageField(upload_to='article_images_small')

    def __str__(self):
        return f'{self.id}. {self.name}'


class Emails(models.Model):
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email


class Suggestions(models.Model):
    theme = models.CharField(max_length=300, null=True)
    date = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} {self.theme}'
