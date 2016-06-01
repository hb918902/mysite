from django.contrib import admin
from .models import Article,Category

from pagedown.widgets import AdminPagedownWidget
from django import forms
# Register your models here.

class ArticleForm(forms.ModelForm):
	content = forms.CharField(widget=AdminPagedownWidget())

	class Meta:
		model = Article
		fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
	form = ArticleForm
	list_display = ['title', 'author', 'cre_date']
	fields = (('title','author'),'content','category',('cre_date','update'))


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)