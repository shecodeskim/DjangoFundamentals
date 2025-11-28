from django.contrib import admin
from .models import Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date', 'price', 'isbn' ]
    list_filter = [ 'author', 'published_date']
    search_fields = ['title', 'author', 'isbn']

# Register your models here.
