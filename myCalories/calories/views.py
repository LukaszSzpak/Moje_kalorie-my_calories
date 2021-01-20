from django.shortcuts import render
from .managers import *
from .sampleData import addData
import datetime
import calories.managers as manager


# Create your views here.


def main_view(request):
    today = datetime.date.today()
    return render(request, "index.html", {"prev_date": today - datetime.timedelta(1),
                                          "act_date": today,
                                          "next_date": today + datetime.timedelta(1),
                                          "food_list": manager.get_all_foods_from_day_with_count(today),
                                          "user_lang": 'pl'
                                          }
                  )


def sample_data(request):
    addData.add_sample_data()
    return render(request, "sampleData.html", {})
