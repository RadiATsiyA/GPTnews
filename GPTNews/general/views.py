from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'general/index.html'
    title = 'Home'


class ArticleView(TitleMixin, TemplateView):
    template_name = 'general/article.html'
    title = 'Article'


class LinksView(TitleMixin, TemplateView):
    template_name = 'general/links.html'
    title = 'Links'


class HelloView(TitleMixin, TemplateView):
    template_name = 'general/hello.html'
    title = 'Hell-o'


class CreateNews(TitleMixin, TemplateView):
    title = 'Create New!'
    template_name = 'general/createnews.html'
