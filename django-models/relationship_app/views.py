from typing import Any
from django.shortcuts import render,redirect
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



# Create your views here.
def list_books(request):
    books = Book.objects.all() #fetching all books from the database
    context = {'list_books':books} #creates a context dictionary with list of books
    return render(request, 'relationship_app/list_books.html', context)

#class-based view for listing books in a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books_list'] = library.get_books_list()
        return context
    

#Setup User Authentication Views

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ("index")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

#User Login View
class CustomLoginView(LoginView):
    template_name = "login.html"

#user Logout View
class CustomLogoutView(LogoutView):
    template_name = "logout.html"

#Homepage View
def index(request):
    return render(request, "index.html")

#Setting Up Role-Based Views

def is_admin(user):
    return user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)

def librarian_view(request):
    return render(request, 'librarian_view.html')

def is_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
