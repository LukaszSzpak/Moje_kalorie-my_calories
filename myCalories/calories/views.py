from django.shortcuts import render
from .models import User


# Create your views here.

def main_view(request):
    return render(request, "index.html", {})
