from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
    
    def clean_author(self):
        author = self.cleaned_data['author']
        return author