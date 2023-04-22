from django.urls import path
from .views import index, all_books, book_detail, favourite_book

urlpatterns = [
    path('', index, name='home-page'),
    path('all_books/', all_books, name='all-books'),
    path('book_detail/<slug:slug>', book_detail, name='book-detail'),
    path('favourite_books/', favourite_book, name='all-fav-books'),
]
