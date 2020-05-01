from django.shortcuts import render, get_object_or_404
from .models import PrivacyPolicy, Review
from .forms import EmailContactForm, PhoneContactForm, BasicContactForm, ValuationForm
from django.core.mail import send_mail
from blog.models import Category, Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def template_sort_function(data):
    if data == 'Google':
        return 'Google Maps'
    elif data == 'Oferia':
        return 'Oferia'
    elif data == 'Oferteo':
        return 'Oferteo'
    elif data == 'Facebook':
        return 'Facebook'
    else:
        return 'Pisemna referencja'

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
    return render(request, 'home.html', context)

def portal(request):
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
    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news': best_news,}
    return render(request, 'portal.html', context)

def shop(request):
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
    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news': best_news,}
    return render(request, 'shop.html', context)

def on_page_website(request):
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
    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news': best_news,}
    return render(request, 'on_page_website.html', context)

def e_marketing(request):
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
    send = False
    if request.method == 'POST':
        form = PhoneContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            topic = 'Klient prosi o kontakt Tel.: %s o godzinie %s' %(cd['number'], cd['data_contact'])
            to = ['biuro@e-bluedesign.co', ]
            send_mail(topic, topic, 'benjamin.langeriaf7@gmail.com', to)
            send = True
    else:
        form = PhoneContactForm()
    if send:
        form = PhoneContactForm()

    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news': best_news,
               'form': form,
               'send': send,
               }
    return render(request, 'e_marketing.html', context)

def contact(request):
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
    send = False
    if request.method == 'POST':
        form = BasicContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            topic = 'Klient %s (%s) wysyla wiadomosc. Tel.: %s' %(cd['e_mail'], cd['name'], cd['phone'])
            massage = 'TYTUL: %s| WIADOMOSC: %s|' % (cd['topic'], cd['context'])
            to = ['biuro@e-bluedesign.co', ]
            send_mail(topic, massage, 'benjamin.langeriaf7@gmail.com', to)
            send = True
    else:
        form = BasicContactForm()
    if send:
        form = BasicContactForm()

    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news': best_news,
               'form': form,
               'send': send}
    return render(request, 'contact.html', context)

def valuation_online(request):
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
    send = False
    if request.method == 'POST':
        form = ValuationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            topic = 'Klient %s (%s) wysyla wiadomosc. Tel.: %s' %(cd['e_mail'], cd['name'], cd['phone'])
            massage = 'TYTUL: %s| WIADOMOSC: %s|' % (cd['type'], cd['context'])
            to = ['biuro@e-bluedesign.co', ]
            send_mail(topic, massage, 'benjamin.langeriaf7@gmail.com', to)
            send = True
    else:
        form = ValuationForm()

    context = {'category_1': category_1,
               'category_2': category_2,
               'category_3': category_3,
               'category_4': category_4,
               'post_category_1': post_category_1,
               'post_category_2': post_category_2,
               'post_category_3': post_category_3,
               'post_category_4': post_category_4,
               'best_news': best_news,
               'form': form,
               'send': send}
    return render(request, 'valuation_online.html', context)

def privacy_policy(request):
    privacy_policy = get_object_or_404(PrivacyPolicy, pk=1)
    context = {'privacy_policy': privacy_policy}
    return render(request, 'privacy_policy.html', context)

def reviews(request):
    #reviews
    sort_reviews = request.GET.get('sort', False)
    reviews = Review.objects.all().order_by('-date')
    count_all_reviews = Review.objects.all().count
    count_oferia =  reviews.filter(place_review='Oferia').count
    count_google = reviews.filter(place_review='Google Maps').count
    count_oferteo = reviews.filter(place_review='Oferteo').count
    count_facebook = reviews.filter(place_review='Facebook').count
    if sort_reviews:
        reviews = reviews.filter(place_review=template_sort_function(sort_reviews))
    #paginator
    page = request.GET.get('page', 1)
    paginator = Paginator(reviews, 5)
    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)
    #get newsleter footer
    best_news = Post.objects.all().order_by('order_number_home_page')[:5]
    context = {'best_news': best_news,
               'numbers': numbers,
               'reviews': reviews,
               'sort_reviews': sort_reviews,
               'count_oferia': count_oferia,
               'count_google': count_google,
               'count_oferteo': count_oferteo,
               'count_facebook': count_facebook,
               'count_all_reviews': count_all_reviews}
    return render(request, 'reviews.html', context)