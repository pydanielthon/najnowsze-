from django.db import models
from ckeditor.fields import RichTextField

class PrivacyPolicy(models.Model):
    content = RichTextField()
    regulations = RichTextField()

class Review(models.Model):
    CHOICES_PLACE_COMMENT = (
        ('Oferia', 'Oferia.pl'),
        ('Google Maps', 'Google Maps'),
        ('Oferteo', 'Oferteo.pl'),
        ('Facebook', 'Facebook'),
        ('Pisemna referencja', 'Pisemna referencja'),
    )
    owner = models.CharField(max_length=250)
    rating = models.IntegerField()
    date = models.DateTimeField()
    url_comment = models.URLField()
    url_media = models.URLField()
    place_review = models.CharField(max_length=250, choices=CHOICES_PLACE_COMMENT, default='Oferia')
    description = models.TextField(blank=True)
    write_reverence = models.BooleanField(default=False)
    reference_img = models.ImageField(blank=True, null=True, verbose_name='Zdjecie o wymiaracj 1200x800')

    def __str__(self):
        return '%s - %s' %(self.owner, self.place_review)