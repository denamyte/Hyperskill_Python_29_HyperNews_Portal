from datetime import datetime
import json
from typing import Dict, List

from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View

from .forms import CreateForm


def read_news() -> List[Dict[str, str | int]]:
    with open(settings.NEWS_JSON_PATH, 'r') as f:
        return json.load(f)


NEWS = read_news()


def sort_by_day(news: List[Dict[str, str | int]], q='') -> List[Dict[str, str | int]]:
    filtered = filter(lambda n: q in n['title'], news) if q else news
    sorted_news = sorted(filtered, key=lambda n: n['created'], reverse=True)
    for n in sorted_news:
        n['day'] = n['created'].split()[0]
    return sorted_news


def coming(request):
    return redirect('/news/')


class MainView(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        by_day = {'by_day': sort_by_day(NEWS, q)}
        return render(request, 'news/main.html', context=by_day)


class ArticleView(View):
    def get(self, request, link: int, *args, **kwargs):
        article = next((a for a in NEWS if link == a['link']), None)
        return render(request, 'news/article.html', context=article)


class CreateNewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/create.html')

    def post(self, request, *args, **kwargs):
        form = CreateForm(request.POST)
        if form.is_valid():
            article = {'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                       'text': form.cleaned_data.get('text'),
                       'title': form.cleaned_data.get('title'),
                       'link': max(n['link'] for n in NEWS) + 1}
            NEWS.append(article)
            with open(settings.NEWS_JSON_PATH, 'w') as f:
                json.dump(NEWS, f)
        return redirect('/news/')
