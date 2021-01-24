from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='index'),
    path('index', views.main_view, name='index'),
    path('sample', views.sample_data),
    path('post/ajax/dayFoodList', views.get_day_food_list, name='dayFoodList'),
    path('post/ajax/allFoodList', views.get_food_list, name='allFoodList'),
    path('post/ajax/getFood', views.get_food, name='getFood'),
    path('post/ajax/addFoodToDay', views.add_food_to_day, name='addFoodToDay'),
    path('post/ajax/addManualFoodToDay', views.add_manual_food_to_day, name='addManualFoodToDay')
]
