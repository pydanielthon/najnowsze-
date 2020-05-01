from django.contrib import admin
from .models import Realization

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Realization, ArticleAdmin)
