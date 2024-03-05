from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
       ordering=('name',)
       verbose_name='category'
       verbose_name_plural='categories'

    def __str__(self):
       return '{}'.format(self.name)

    def get_url(self):
        return reverse('movie:movies_by_category',args=[self.slug])


class movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    img = models.ImageField(upload_to='movies')
    date = models.DateField()
    actors = models.TextField(max_length=250)
    youtube_link = models.URLField(blank=True, null=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)


    class Meta:
       ordering=('name',)
       verbose_name='movie'
       verbose_name_plural='movies'


    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


