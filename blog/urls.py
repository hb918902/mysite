from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^p/(?P<article_id>[0-9]+)/$', views.detail,name='detail'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.my_login, name='my_login'),
    url(r'^logout/$',views.my_logout, name='my_logout'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name="category"),
]