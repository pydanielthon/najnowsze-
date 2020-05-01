from django.shortcuts import render
from en_blog.models import Category, Post


def home(request):
    #must by
    category = Category.objects.all()
    try:
        category_1 = category[0]
    except:
        category_1 = 'Dla nowicjuszy'
    try:
        category_2 = category[1]
    except:
        category_2 = 'Technologie'
    try:
        category_3 = category[2]
    except:
        category_3 = 'Realizacje'
    try:
        category_4 = category[3]
    except:
        category_4 = 'Promocja'
    post_category_1 = Post.objects.filter(category=category_1)[:5]
    post_category_2 = Post.objects.filter(category=category_2)[:2]
    post_category_3 = Post.objects.filter(category=category_3)[:3]
    post_category_4 = Post.objects.filter(category=category_4)[:3]
    #get newsleter footer
    best_news = Post.objects.all().order_by('order_number_home_page')[:5]
    try:
        best_news_1 = best_news[0]
    except:
        best_news_1 = None
    try:
        best_news_2 = best_news[1]
    except:
        best_news_2 = None
    try:
        best_news_3 = best_news[2]
    except:
        best_news_3 = None
    try:
        best_news_4 = best_news[3]
    except:
        best_news_4 = None
    try:
        best_news_5 = best_news[4]
    except:
        best_news_5 = None


    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news_1': best_news_1,
               'best_news_2': best_news_2,
               'best_news_3': best_news_3,
               'best_news_4': best_news_4,
               'best_news_5': best_news_5,
               'best_news': best_news,
               }
    return render(request, 'en_app/home.html', context)
