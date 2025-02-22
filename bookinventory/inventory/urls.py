from django.urls import path
from .views import add_book, book_list, update_book, delete_book

urlpatterns = [
    path('', add_book, name='add_book'),
    path('books/', book_list, name='book_list'),
    path('update/<int:book_id>/', update_book, name='update_book'),
    path('delete/<int:book_id>/', delete_book, name='delete_book'),
]
