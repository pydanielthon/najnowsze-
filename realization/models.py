from django.db import models
from django_resized import ResizedImageField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

class Realization(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    img = ResizedImageField(size=[480, 320], crop=['middle', 'center'])
    logo = models.ImageField()
    trade = models.CharField(max_length=100)
    goal = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    content = RichTextUploadingField()
    opinion = models.CharField(max_length=200)
    opinion_owner = models.CharField(max_length=100)
    opinion_owner_position = models.CharField(max_length=100)

    def __str__(self):
        return self.title