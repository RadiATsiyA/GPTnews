from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'general/index.html'


class ArticleView(TemplateView):
    template_name = 'general/article.html'


class LinksView(TemplateView):
    template_name = 'general/links.html'


class HelloView(TemplateView):
    template_name = 'general/hello.html'
