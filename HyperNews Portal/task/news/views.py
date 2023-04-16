import json
from typing import Dict, List

from django.conf import settings
from django.shortcuts import render
from django.views import View


def read_news() -> List[Dict[str, str | int]]:
    with open(settings.NEWS_JSON_PATH, 'r') as f:
        return json.load(f)


NEWS = read_news()


def sort_by_day(news: List[Dict[str, str | int]]) -> List[Dict[str, str | int]]:
    sorted_news = sorted(news, key=lambda n: n['created'], reverse=True)
    for n in sorted_news:
        n['day'] = n['created'].split()[0]
    return sorted_news


def coming(request):
    return render(request, 'news/index.html')


class MainView(View):
    def get(self, request, *args, **kwargs):
        by_day = {'by_day': sort_by_day(NEWS)}
        return render(request, 'news/main.html', context=by_day)


class ArticleView(View):
    def get(self, request, link: int, *args, **kwargs):
        article = next((a for a in NEWS if link == a['link']), None)
        return render(request, 'news/article.html', context=article)
