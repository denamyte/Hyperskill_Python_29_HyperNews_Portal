import json
from typing import Dict, List

from django.conf import settings
from django.shortcuts import render
from django.views import View


def read_news() -> List[Dict[str, str | int]]:
    with open(settings.NEWS_JSON_PATH, 'r') as f:
        return json.load(f)


NEWS = read_news()


def sort_by_day(news: List[Dict[str, str | int]]) -> Dict[str, List[Dict[str, str | int]]]:
    key_set = {n['created'].split()[0] for n in news}
    keys = sorted(key_set, reverse=True)
    by_day = {}

    for key in keys:
        by_day[key] = sorted([n for n in news if key in n['created']],
                             reverse=True,
                             key=lambda n: n['created'])
    return by_day


def coming(request):
    return render(request, 'news/index.html')


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {'by_day': sort_by_day(NEWS)}
        return render(request, 'news/main.html', context=context)


class ArticleView(View):
    def get(self, request, link: int, *args, **kwargs):
        article = next((a for a in NEWS if link == a['link']), None)
        return render(request, 'news/article.html', context=article)
