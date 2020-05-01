from django.contrib import admin
from .models import Category, Post, Comment, KeyWords

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Post, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(KeyWords)
