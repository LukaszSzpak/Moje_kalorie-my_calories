import json
import pickle

from django.http import JsonResponse
from django.shortcuts import render

from .ResponseFood import ResponseFood
from .managers import *
from .sampleData import addData
import datetime
import calories.managers as manager
from calories.services.dateConvertion import string_to_date, date_to_string, yesterday, tommorow


# Create your views here.

def main_view(request):


    today = datetime.date.today()
    return render(request, "index.html", {"prev_date": date_to_string(yesterday(today)),
                                          "act_date": date_to_string(today),
                                          "next_date": date_to_string(tommorow(today)),
                                          "food_list": manager.get_all_foods_from_day_with_count(today),
                                          "user_lang": 'pl'
                                          }
                  )


def sample_data(request):
    addData.add_sample_data()
    return render(request, "sampleData.html", {})


def get_food_list(request):
    if request.is_ajax and request.method == "POST":
        data = request.POST.dict()
        this_day = string_to_date(data['date'])

        my_response = []
        for food, unit in manager.get_all_foods_from_day_with_count(this_day):
            my_response.append(ResponseFood(food, unit))

        json_string = json.dumps([ob.__dict__ for ob in my_response])

        return JsonResponse({"food_list": json_string,
                             "prev_date": date_to_string(yesterday(this_day)),
                             "act_date": date_to_string(this_day),
                             "next_date": date_to_string(tommorow(this_day))}, status=200)
