# coding=utf-8

from .models import Article,Category
from django.db.models import Count


def month_list(request):
    articles = Article.objects.all()
    year_month = set()
    for a in articles:
        year_month.add((a.cre_date.year,a.cre_date.month))
    counter = {}.fromkeys(year_month,0)
    for a in articles:
        counter[(a.cre_date.year,a.cre_date.month)] += 1
    year_month_number = []
    for key in counter:
        year_month_number.append([key[0],key[1],counter[key]])
    year_month_number.sort(reverse=True)
    return {'year_month_number': year_month_number}


def category(request):
    category1 = Category.objects.annotate(num_article=Count('article'))
    return {"categories": category1}