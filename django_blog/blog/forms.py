
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def register(self, commit=True):
        user = super(CustomUserCreationForm, self).register(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
         user.save()
        return user