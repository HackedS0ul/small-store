from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, FormView
from .models import Book
#new
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .forms import BookForm



class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'create.html'
    fields = [
            'name',
            'isbn_number',
            'description',
            'author',
            'in_store',
            'pub_date',
        ]
    success_url = "/"


class IndexView(ListView):
    model= Book
    template_name= 'listview.html'


class BookDetailView(DetailView):
    model = Book
    template_name = "details.html"

class BookUpdateView(PermissionRequiredMixin,UpdateView):
    model = Book
    template_name = 'update.html'
    fields = [
          'name',
            'isbn_number',
            'description',
            'author',
            'in_store',
            'pub_date',
        ]
    success_url = "/"
    permission_required = 'core.update'


# if user.is_staff (is_active, is_authenticated)
class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'delete.html'
    fields = ["name","isbn_number" ]
    success_url = "/"
    permission_required = 'core.delete'


class ProfileUpdate(UpdateView):
    model = User
    template_name = "profile.html"
    fields = [
        'username',
        'email',
    ]
    success_page= "/"


def loginas(request):
    return render(request, "login.html")





