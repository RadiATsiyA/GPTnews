from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=300)
    text = models.TextField(max_length=3500)
    date = models.DateField(auto_now_add=True)
    image_url = models.URLField(max_length=100, null=True)

    def __str__(self):
        return f'{self.id} | {self.name}'


class Emails(models.Model):
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} | {self.email} | {self.date}'


class Suggestions(models.Model):
    theme = models.CharField(max_length=300, null=True)
    date = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id} | {self.theme} | {self.date}'
