from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from datetime import datetime
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=50)
    order_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    author_img = ResizedImageField(size=[100, 100], crop=['middle', 'center'], blank=True, null=True)
    title = models.CharField(max_length=250)
    navigation_title = models.CharField(max_length=25)
    subtitle = models.CharField(max_length=400)
    img_post_detail = ResizedImageField(verbose_name='Zdjecie glowne szczegoly posta:', size=[1920, 800], crop=['middle', 'center'])
    slug = models.SlugField(unique=True)
    img = ResizedImageField(size=[900, 450], crop=['middle', 'center'])
    content = RichTextField()
    date = models.DateTimeField(default=datetime.now())
    new = models.BooleanField(default=False)
    home = models.BooleanField(default=False)
    home_img = ResizedImageField(size=[400, 500], crop=['middle', 'center'], blank=True, null=True)
    order_number = models.IntegerField(default=0)
    order_number_home_page = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.title, self.category)

class KeyWords(models.Model):
    owner = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    owner = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    content = models.TextField()
    visible = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.email
