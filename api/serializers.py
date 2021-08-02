from book.models import Author, Book, Publisher
from rest_framework import serializers


# Serializers define the API representation.
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    uri = serializers.SerializerMethodField('get_uri')
    number_books = serializers.SerializerMethodField('get_number_books')

    class Meta:
        model = Author
        fields = ['id', 'firstname', 'lastname', 'biography', 'uri', 'photo', 'number_books']

    def get_uri(self, obj):
        return f'/authors/{obj.slug}/'

    def get_number_books(self, obj):
        return obj.number_books()


class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'url', 'description', 'logo']


class BookSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField('get_uri')
    publisher = PublisherSerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'rating', 'isbn', 'pages', 'publisher', 'authors', 'uri', 'front']

    def get_uri(self, obj):
        return f'/books/{obj.slug}/'
