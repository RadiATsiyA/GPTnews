from django.contrib import admin

from general.models import Article, Suggestions, Emails

# Register your models here.
admin.site.register(Article)
admin.site.register(Emails)
admin.site.register(Suggestions)
