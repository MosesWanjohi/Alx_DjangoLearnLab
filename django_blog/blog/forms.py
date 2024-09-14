
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def register(self, commit=True):
        user = super(CustomUserCreationForm, self).register(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
         user.save()
        return user

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if not content:
            raise forms.ValidationError("Content is a required field")
        return content