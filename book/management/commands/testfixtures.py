import random
import time

from django.core.management.base import BaseCommand, CommandError
from book.models import Author, Book, Publisher

from ._private import (rand_authors, authors, publishers, rand_isbn, rand_number_authors, rand_pages, rand_rating,
                       titles, rand_publisher_id)


class Command(BaseCommand):
    help = 'Add fixtures to database'

    def delete(self):
        Book.objects.all().delete()
        Author.objects.all().delete()
        Publisher.objects.all().delete()

    def handle(self, *args, **options):
        random.seed(time.time())
        self.delete()
        num_books = num_authors = num_publishers = 0

        for firstname, lastname in authors():
            try:
                author = Author.objects.get(firstname=firstname, lastname=lastname)
            except Author.DoesNotExist:
                author = Author(firstname=firstname, lastname=lastname)
                author.save()
                num_authors += 1

        for publisher in publishers():
            obj, create = Publisher.objects.get_or_create(
                name=publisher['name'],
                defaults={'url': publisher['url'],
                          'description': publisher['description']}
            )

            if create:
                num_publishers += 1

        for title in titles():
            try:
                book = Book.objects.get(title=title)
            except Book.DoesNotExist:
                book = Book(title=title, isbn=rand_isbn(), rating=rand_rating(), pages=rand_pages())
                book.save()
                num_books += 1

        authors_ = Author.objects.order_by('-pk').all()
        publishers_ids = Publisher.objects.values_list('pk', flat=True)

        for book in Book.objects.all():
            if book.authors.count():
                continue

            numa_max = authors_.first().pk
            numa_min = authors_.last().pk
            publisher = Publisher.objects.get(pk=rand_publisher_id(publishers_ids))
            book.authors.set(authors_.filter(
                pk__in=[random.randint(numa_min, numa_max)
                        for _ in range(rand_number_authors())]))
            book.publisher = publisher
            book.save()

        self.stdout.write(f'Dodano: {num_books} książek, {num_authors} autorów i {num_publishers} wydawców')
        self.stdout.write(self.style.SUCCESS('OK'))
