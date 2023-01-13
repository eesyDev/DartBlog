from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('#', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('#', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='post/')
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL(), null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('#', kwargs={'slug': self.slug})

    class Meta:
        oredering = ['-create_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'