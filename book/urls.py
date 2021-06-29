from django.urls import path

from book.views import AuthorListView, BookListView, PublisherListView, AuthorDetailView, BookDetailView, PublisherDetailView

app_name = 'book'
urlpatterns = [
    path('autorzy/', AuthorListView.as_view(), name='author-list'),
    path('autorzy/<slug:slug>/', AuthorDetailView.as_view(), name='author-detail'),
    path('wydawcy/', PublisherListView.as_view(), name='publisher-list'),
    path('wydawcy/<slug:slug>/', PublisherDetailView.as_view(), name='publisher-detail'),
    path('', BookListView.as_view(), name='book-list'),
    path('ksiazka/<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
]


