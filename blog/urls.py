from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexListView.as_view(), name='index'),
    url(r'^main/(?P<pk>[0-9]+)/$', views.ArticleDetailView.as_view(),name='detail'),
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.my_login, name='my_login'),
    url(r'^logout/$',views.my_logout, name='my_logout'),
    url(r'^category/(\w+)/$', views.CategoryView.as_view(), name="category"),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        views.ArticleMonthArchiveView.as_view(month_format='%m'),
        name="index_by_month"),
    url(r'^ziliao/$', views.ziliao),

]