from django.shortcuts import render
from django.views.generic.list import ListView
from .models import FAQ

# Create your views here.
class FaqList(ListView):
    model = FAQ
    