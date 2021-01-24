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
from calories.services.translation import translate_polish_to_english, translate_english_to_polish
from calories.services.textCoversion import upper_first_letter
from calories.services.wolfram import get_food_data_from_wolfram

__DEFAULT_USER = 'default@user'


# Create your views here.

def main_view(request):
    today = datetime.date.today()
    user = manager.get_user(__DEFAULT_USER)
    return render(request, "index.html", {"prev_date": date_to_string(yesterday(today)),
                                          "act_date": date_to_string(today),
                                          "next_date": date_to_string(tommorow(today)),
                                          "food_list": manager.get_all_foods_from_day_with_count(today),
                                          "user_lang": user.lang,
                                          }
                  )


def sample_data(request):
    addData.add_sample_data()
    return render(request, "sampleData.html", {})


def user_settings_view(request):
    user = manager.get_user(__DEFAULT_USER)
    return render(request, "userSettings.html", {'user': user,
                                                 'user_lang': user.lang})


def update_user_settings(request):
    if request.is_ajax and request.method == "POST":
        data = request.POST.dict()

        manager.change_user(__DEFAULT_USER,
                            float(data['calories']),
                            float(data['fat']),
                            float(data['carbohydrates']),
                            float(data['protein']),
                            float(data['height']),
                            float(data['weight']),
                            data['sex'],
                            data['lang'])

        return JsonResponse({}, status=200)


def get_day_food_list(request):
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


def get_food_list(request):
    if request.is_ajax and request.method == "POST":
        json_string = json.dumps([ResponseFood(ob, 0).__dict__ for ob in manager.get_all_foods()])

        return JsonResponse({"food_list": json_string}, status=200)


def add_food_to_day(request):
    if request.is_ajax and request.method == "POST":
        data = request.POST.dict()
        lang = data['lang']
        food_name = data['food_name']
        count = float(data['count'])
        date = string_to_date(data['date'])

        if lang == "pl":
            food_name = translate_polish_to_english(food_name)

        food_name = upper_first_letter(food_name)
        manager.add_food_to_day(manager.get_day(date),
                                manager.get_food(food_name),
                                count)

        return JsonResponse({}, status=200)


def get_food(request):
    if request.is_ajax and request.method == "POST":
        data = request.POST.dict()
        lang = data['lang']
        food_name = data['food_name']

        if lang == "pl":
            food_name = translate_polish_to_english(food_name)

        json_string = json.dumps(ResponseFood(manager.get_food(food_name), 0).__dict__)
        return JsonResponse({"food": json_string}, status=200)


def add_manual_food_to_day(request):
    if request.is_ajax and request.method == "POST":
        data = request.POST.dict()

        lang = data['lang']
        date = string_to_date(data['date'])
        food_name = data['food_name']

        if lang == "pl":
            food_name_pl = upper_first_letter(food_name)
            food_name = upper_first_letter(translate_polish_to_english(food_name))
        else:
            food_name_pl = upper_first_letter(translate_english_to_polish(food_name))
            food_name = upper_first_letter(food_name)

        new_food = manager.add_or_change_food(food_name,
                                              food_name_pl,
                                              data['food_unit'],
                                              float(data['food_calories']),
                                              float(data['food_fat']),
                                              float(data['food_carbohydrates']),
                                              float(data['food_protein']))

        manager.add_food_to_day(manager.get_day(date), new_food, float(data['food_count']))

        return JsonResponse({}, status=200)


def add_wolfram_food_to_day(request):
    if request.is_ajax and request.method == "POST":
        data = request.POST.dict()

        lang = data['lang']
        date = string_to_date(data['date'])
        food_name = data['food_name']

        if lang == "pl":
            food_name_pl = upper_first_letter(food_name)
            food_name = upper_first_letter(translate_polish_to_english(food_name))
        else:
            food_name_pl = upper_first_letter(translate_english_to_polish(food_name))
            food_name = upper_first_letter(food_name)

        new_food = get_food_data_from_wolfram(food_name, data['food_unit'])
        new_food.name_pl = food_name_pl
        manager.save_food(new_food)

        manager.add_food_to_day(manager.get_day(date), new_food, float(data['food_count']))
        return JsonResponse({}, status=200)
