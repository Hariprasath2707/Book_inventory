from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book
from .forms import BookForm, BookUpdateForm

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect('book_list')  
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def update_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)

    if request.method == 'POST':
        form = BookUpdateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect('book_list')  
    else:
        form = BookUpdateForm(instance=book)

    return render(request, 'update_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, book_id=book_id)

    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect('book_list') 

    return render(request, 'confirm_delete.html', {'book': book})
