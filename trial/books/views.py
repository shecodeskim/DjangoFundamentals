from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Book
from .forms import BookForm

def book_list(request):
    """
    Display all books in the database
    """
    books = Book.objects.all().order_by('-id')  # Newest books first
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    """
    Display details of a specific book
    """
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})

def book_create(request):
    """
    Create a new book
    """
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" was created successfully!')
            return redirect('book_detail', pk=book.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm()
    
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    """
    Update an existing book
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" was updated successfully!')
            return redirect('book_detail', pk=book.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'books/book_form.html', {'form': form})

def book_delete(request, pk):
    """
    Delete a book
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == "POST":
        book_title = book.title
        book.delete()
        messages.success(request, f'Book "{book_title}" was deleted successfully!')
        return redirect('book_list')
    
    return render(request, 'books/book_confirm_delete.html', {'book': book})