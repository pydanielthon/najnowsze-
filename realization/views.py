from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import Post, Category
from .models import Realization
import random

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
    #more
    objects = Realization.objects.all()
    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news': best_news,
               'objects': objects}
    return render(request, 'realization/list-realization.html', context)

def realization(request, slug):
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
    #more
    object = get_object_or_404(Realization, slug=slug)
    try:
        random_objects = random.sample(list(Realization.objects.exclude(id=object.id)), 3)
    except:
        random_objects = None
    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news': best_news,
               'object': object,
               'random_objects': random_objects}
    return render(request, 'realization/single-realization.html', context)