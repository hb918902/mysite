# -*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404

from django.contrib import auth
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from django.views.generic.dates import MonthArchiveView
from django.views.generic import ListView, DetailView

from .models import Article, Category


# Create your views here.

PAGENUM = 10


class IndexListView(ListView):
    queryset = Article.objects.all().order_by('cre_date')
    template_name = 'blog/main/index.html'
    context_object_name = 'articles'
    paginate_by = PAGENUM


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'blog/main/detail.html'


class CategoryView(ListView):
    template_name = 'blog/main/index.html'
    paginate_by = PAGENUM
    context_object_name = 'articles'

    def get_queryset(self):
        category = get_object_or_404(Category, name=self.args[0])
        return Article.objects.filter(category=category)


class ArticleMonthArchiveView(MonthArchiveView):
    template_name = 'blog/main/index.html'
    queryset = Article.objects.all()
    date_field = "cre_date"
    context_object_name = 'articles'
    paginate_by = PAGENUM


def ziliao(request):
    return render(request,'blog/main/ziliao.html')



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


def my_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog/')



