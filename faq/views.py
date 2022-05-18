from django.shortcuts import render
from django.views.generic.list import ListView
from .models import FAQ

class FaqList(ListView):
    model = FAQ
    