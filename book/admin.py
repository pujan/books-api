from django.contrib import admin

from .models import Author, Publisher, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #list_display = ('firstname', 'lastname')
    #fields = []
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    #list_display = ('name',)
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    #list_display = ('title', 'rating')
    pass

