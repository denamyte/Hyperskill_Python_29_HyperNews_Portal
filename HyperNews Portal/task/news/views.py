from typing import Dict, List

from django.views import View
from django.shortcuts import render
from django.conf import settings
import json


def coming(request):
    return render(request, 'news/index.html')


def read_news() -> List[Dict[str, str | int]]:
    with open(settings.NEWS_JSON_PATH, 'r') as f:
        return json.load(f)


class ArticleView(View):
    def get(self, request, link: int, *args, **kwargs):
        news = read_news()
        article = next((a for a in news if link == a['link']), None)
        return render(request, 'news/article.html', context=article)
