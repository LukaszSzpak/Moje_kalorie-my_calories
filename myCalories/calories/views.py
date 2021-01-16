from django.shortcuts import render
from .managers import *
from .sampleData import addData
import datetime


# Create your views here.


def main_view(request):
    return render(request, "index.html", {'foods': get_all_foods(), 'days': get_all_days()})


def sample_data(request):
    return render(request, "sampleData.html", {})
