from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login, views
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

#User registration view
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
     
#User login view

class LoginView(views.LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/login.html'


#User logout view
LoginRequiredMixin(login_url='login')
class LogoutView(views.LogoutView):
    success_url = reverse_lazy('login')


