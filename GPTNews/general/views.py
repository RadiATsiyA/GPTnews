import openai

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from common.views import TitleMixin

from general.models import Article


class IndexView(TitleMixin, ListView):
    model = Article
    template_name = 'general/index.html'
    title = 'Home'
    paginate_by = 6


class ArticleView(TitleMixin, DetailView):
    model = Article
    template_name = 'general/article.html'
    context_object_name = 'article'
    title = 'Article'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['article'] = Article.objects.filter(id=id)


class LinksView(TitleMixin, TemplateView):
    template_name = 'general/links.html'
    title = 'Links'


class HelloView(TitleMixin, TemplateView):
    template_name = 'general/hello.html'
    title = 'Hell-o'


class CreateNews(TitleMixin, View):
    def get(self, request):
        return render(request, 'general/createnews.html')

    def post(self, request):
        context = {}
        model_engine = 'gpt-3.5-turbo-0301' #'text-davinci-003'
        max_tokens = 500

        if request.method == 'POST':
            theme = request.POST['theme']
            promt = f'Generate fantastic news, and write an article for 300 words on topic {theme}'

            completion = openai.Completion.create(engine=model_engine, promt=promt, max_tokets=max_tokens)
            chatResponse = completion.choices[0].text

            context = {
                'chatResponse': chatResponse,
                'promt': promt
            }
            return render(request, 'general/createnews.html', context)

        else:
            context["raise_error"] = "ERROR Occured or something went wrong."
        return redirect('create_news')
