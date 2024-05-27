from django.contrib import admin

# Register your models here.
from article.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # search_fields = ('title__startswith',)
    fields = ('title', 'content', 'image', 'read_time', 'is_active', 'is_special',)
