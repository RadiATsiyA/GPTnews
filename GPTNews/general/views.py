import openai

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.conf import settings
from django.core.cache import cache

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from common.views import TitleMixin

from general.models import Article, Emails

from general.forms import EmailForm, SuggestionForm

from craiyon import Craiyon


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

    def get_context_data(self, **kwargs):
        cache_key = f"article/{self.kwargs['pk']}"
        article = cache.get(cache_key)
        if not article:
            article = super().get_context_data()
            cache.set(cache_key, article, 43200)
        context = article
        context['next_articles'] = Article.objects.order_by('date')[:6]
        context['form'] = EmailForm()
        return context

    def post(self, request, *args, **kwargs):
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            email_obj = Emails(email=email)
            email_obj.save()
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            print(form.errors)
        return render(request, self.template_name, self.get_context_data())


class LinksView(TitleMixin, TemplateView):
    template_name = 'general/links.html'
    title = 'Links'


class HelloView(TitleMixin, TemplateView):
    template_name = 'general/hello.html'
    title = 'Hell-o'


class CreateNews(TitleMixin, View):
    def get(self, request, **kwargs):
        context = {
            'form': SuggestionForm()
        }
        return render(request, 'general/createnews.html', context)

    def post(self, request):
        generator = Craiyon()
        if request.method == 'POST':
            openai.api_key = settings.OPENAI_API_KEY
            form = SuggestionForm(request.POST)
            theme = 'any topic'
            if form.is_valid():
                theme = form.cleaned_data['theme']
            else:
                print(form.errors)
            prompt = f'Generate a fantastic news and write an article for 230 words, on topic "{theme}"'

            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=prompt,
                max_tokens=300,
                temperature=1
            )
            result = generator.generate(f"{theme}", negative_prompt="spoon", model_type="art")
            url = result.images.pop(0)

            article_obj = Article(name=theme, text=response['choices'][0]['text'], image_url=url)
            article_obj.save()
            return HttpResponseRedirect(reverse_lazy('article', kwargs={'pk': article_obj.id}))
        return render(request, 'general/createnews.html')
