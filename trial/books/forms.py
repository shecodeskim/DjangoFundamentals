from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'price']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'isbn': forms.TextInput(attrs={'placeholder': 'Enter 13-digit ISBN'}),
            'price': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01'}),
        }
    
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        if isbn and len(isbn) != 13:
            raise forms.ValidationError("ISBN must be exactly 13 digits.")
        return isbn