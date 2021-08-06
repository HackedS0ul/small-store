

from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('create/', BookCreateView.as_view(), name="create"),
    path('details/<pk>/', BookDetailView.as_view(), name="view"),
    path('update/<pk>/', BookUpdateView.as_view(), name="update"),
    path('delete/<pk>/', BookDeleteView.as_view(), name="delete"),
    path('profile/<pk>/', ProfileUpdate.as_view(), name="profile"),
    path('login/', views.loginas, name="login"),
    
]
