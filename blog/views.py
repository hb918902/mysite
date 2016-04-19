# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404

from .models import Article

# Create your views here.

def index(request):
    latest_article_list = Article.objects.order_by('update')[:5]
    context = {'latest_article_list':  latest_article_list}
    return render(request, 'blog/index.html',context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/p/detail.html', {'article': article})
