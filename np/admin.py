from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
	list_display = ['title', 'section', 'author', 'created_date']

# Register your models here.
admin.site.register(Article, ArticleAdmin)