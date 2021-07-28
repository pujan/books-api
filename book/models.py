from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


def slug(instance):
    return '-'.join([instance.firstname, instance.lastname])


class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)
    # photo = models.ImageField(upload_to='authors')
    slug = AutoSlugField(populate_from=slug, unique=True, null=True)

    class Meta:
        ordering = ['firstname', 'lastname']
        verbose_name = 'autor'
        verbose_name_plural = 'autorzy'

    def get_absolute_url(self):
        return reverse('book:author-detail', args=[self.slug])

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Publisher(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=50)
    description = models.TextField(null=True, blank=True)
    # logo = models.ImageField(upload_to='images/books')
    slug = AutoSlugField(populate_from='name', unique=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'wydawca'
        verbose_name_plural = 'wydawcy'

    def get_absolute_url(self):
        return reverse('book:publisher-detail', args=[self.slug])

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, related_name='books')
    isbn = models.CharField(max_length=15)
    pages = models.IntegerField()
    rating = models.FloatField(default=0.0)
    publisher = models.ForeignKey(Publisher, related_name='book', on_delete=models.CASCADE, null=True)
    # front = models.ImageField(upload_to='images/books')
    slug = AutoSlugField(populate_from='title', unique=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'książka'
        verbose_name_plural = 'książki'

    def get_absolute_url(self):
        return reverse('book:book-detail', args=[self.slug])

    def __str__(self):
        return self.title
