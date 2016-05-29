# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from django.views.generic.dates import MonthArchiveView

from .models import Article, Category

from django.db.models import Count

# Create your views here.

# 用于侧边栏月份文章归档统计
def month_list():
    articles = Article.objects.all()
    year_month = set()
    for a in articles:
        year_month.add((a.cre_date.year,a.cre_date.month))
    counter = {}.fromkeys(year_month,0)
    for a in articles:
        counter[(a.cre_date.year,a.cre_date.month)]+=1
    year_month_number = []
    for key in counter:
        year_month_number.append([key[0],key[1],counter[key]])
    year_month_number.sort(reverse=True)
    return {'year_month_number':year_month_number}




# blog首页
def index(request):
    # latest_article_list = Article.objects.order_by('update')[:5]
    # context = {'latest_article_list':  latest_article_list}
    # return render(request, 'blog/index.html',context)
    # 重写完成分页功能
    article_list = Article.objects.all().order_by('cre_date')
    paginator = Paginator(article_list, 4)  # show 4 articles per page

    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # 页码不是整数，返回第一页。
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    d_key = {"articles": articles,
    "is_category": False,
    "categories": Category.objects.annotate(num_article=Count('article'))}

    d_key.update(month_list())  # 合并月份

    return render(request, 'blog/main/index.html', d_key)

# 文章详细
def detail(request,article_id):
    article = get_object_or_404(Article, pk=article_id)

    d_key = {"article": article,
    "is_category": False,
    "categories": Category.objects.annotate(num_article = Count('article'))}

    d_key.update(month_list())

    return render(request, 'blog/main/detail.html', d_key)


# 用户注册
@csrf_exempt
def register(request):
    errors = []
    account = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    if request.method == 'POST':
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors.append('密码不能为空')
        else:
            password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append('确认密码不能为空')
        else:
            password2 = request.POST.get('password2')
        if not request.POST.get('email'):
            errors.append('邮箱不能为空')
        else:
            email = request.POST.get('email')

        if password is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append('两次输入密码不一致')

        if account is not None and password is not None and password2 is not None and email is not None and CompareFlag :
            user = User.objects.create_user(account,email,password)
            user.save()

            userlogin = auth.authenticate(username = account,password = password)
            auth.login(request,userlogin)
            return HttpResponseRedirect('/blog')

    return render(request,'blog/register.html', {'errors': errors})


# 用户登录
@csrf_exempt
def my_login(request):
    errors =[]
    account = None
    password = None
    if request.method == "POST":
        if not request.POST.get('account'):
            errors.append('用户名不能为空')
        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            errors = request.POST.get('密码不能为空')
        else:
            password = request.POST.get('password')

        if account is not None and password is not None:
            user = auth.authenticate(username=account,password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request,user)
                    return HttpResponseRedirect('/blog')
                else:
                    errors.append('用户名错误')
            else:
                errors.append('用户名或密码错误')
    return render(request,'blog/login.html', {'errors': errors})

# 用户退出
def my_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog')


# 文章分类
def category(request, pk):

    cate = Category.objects.get(pk=pk)
    article_list = cate.article_set.all()

    paginator = Paginator(article_list,4) #show 4 articles per page

    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        #页码不是整数，返回第一页。
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    d_key = {"article_list":article_list,
    "articles": articles,
    "is_category": True,
    "cate_name": cate.name,
    "categories": Category.objects.annotate(num_article = Count('article'))}

    d_key.update(month_list())

    return render(request, 'blog/main/index.html', d_key)



# 月份归档
class ArticleMonthArchiveView(MonthArchiveView):
    template_name = 'blog/main/index_by_month.html'
    queryset = Article.objects.all()
    date_field = "cre_date"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(ArticleMonthArchiveView,self).get_context_data(**kwargs)
        context["categories"] = Category.objects.annotate(num_article = Count('article'))
        context.update(month_list())
        return context

