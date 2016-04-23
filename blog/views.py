# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .models import Article

# Create your views here.

def index(request):
    # latest_article_list = Article.objects.order_by('update')[:5]
    # context = {'latest_article_list':  latest_article_list}
    # return render(request, 'blog/index.html',context)
    article_list = Article.objects.all().order_by('cre_date')
    paginator = Paginator(article_list,4) #show 2 articles per page

    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        #页码不是整数，返回第一页。
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'blog/index.html', {'articles': articles})






def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/p/detail.html', {'article': article})
