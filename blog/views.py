from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    #must by
    category = Category.objects.all()
    posts_query = Post.objects.all()
    # paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_query, 8) #5 okrela ile elementow na steonie
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

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
    post_category_4 = Post.objects.filter(category=category_4)[:4]
    #get newsleter footer
    best_news = Post.objects.all().order_by('order_number_home_page')[:5]
    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news': best_news,
               'category': category,
               'posts': posts}
    return render(request, 'blog/post_list.html', context)

def single_post(request, slug):
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
    object = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.filter(owner=object)
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
               'comment': comment}
    return render(request, 'blog/single_post.html', context)