from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField


def slug(instance):
    """For migration 0007"""
    return '-'.join([instance.firstname, instance.lastname])


def lower_and_replace(text):
    return text.lower().replace('ł', 'l').replace(' ', '-')


def author_slug(instance):
    return '-'.join([lower_and_replace(instance.firstname), lower_and_replace(instance.lastname)])


def book_slug(instance):
    return lower_and_replace(instance.title)


def publisher_slug(instance):
    return lower_and_replace(instance.name)


class Author(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    biography = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='images/authors', default=None, blank=True, null=True)
    slug = AutoSlugField(populate_from=author_slug, unique=True, null=True)

    class Meta:
        ordering = ['firstname', 'lastname']
        verbose_name = 'autor'
        verbose_name_plural = 'autorzy'

    def get_absolute_url(self):
        return reverse('book:author-detail', args=[self.slug])

    def number_books(self):
        return len(self.books.all())

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Publisher(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=50)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='images/books', default=None, blank=True, null=True)
    slug = AutoSlugField(populate_from=publisher_slug, unique=True, null=True)

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
    front = models.ImageField(upload_to='images/books', default=None, blank=True, null=True)
    slug = AutoSlugField(populate_from=book_slug, unique=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'książka'
        verbose_name_plural = 'książki'

    def get_absolute_url(self):
        return reverse('book:book-detail', args=[self.slug])

    def __str__(self):
        return self.title
