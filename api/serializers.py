from rest_framework import serializers
from book.models import Author, Publisher, Book


# Serializers define the API representation.
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    uri = serializers.SerializerMethodField('get_uri')

    class Meta:
        model = Author
        fields = ['id', 'firstname', 'lastname', 'biography', 'uri']

    def get_uri(self, obj):
        return f'/authors/{obj.slug}/'

class PublisherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'url', 'description']


class BookSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField('get_uri')
    publisher = PublisherSerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'rating', 'isbn', 'pages', 'publisher', 'authors', 'uri']

    def get_uri(self, obj):
        return f'/books/{obj.slug}/'
