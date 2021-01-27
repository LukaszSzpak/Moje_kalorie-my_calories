from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='index'),
    path('index', views.main_view, name='index'),
    path('sample', views.sample_data),
    path('userSettings', views.user_settings_view, name='userSettings'),
    path('weekly', views.weekly_view, name='weekly'),
    path('post/ajax/dayFoodList', views.get_day_food_list, name='dayFoodList'),
    path('post/ajax/allFoodList', views.get_food_list, name='allFoodList'),
    path('post/ajax/getFood', views.get_food, name='getFood'),
    path('post/ajax/addFoodToDay', views.add_food_to_day, name='addFoodToDay'),
    path('post/ajax/addManualFoodToDay', views.add_manual_food_to_day, name='addManualFoodToDay'),
    path('post/ajax/addWolframFoodToDay', views.add_wolfram_food_to_day, name='addWolframFoodToDay'),
    path('post/ajax/userSettingsForm', views.update_user_settings, name='userSettingsForm'),
    path('post/ajax/weeklySummary', views.get_weekly_summary, name='weeklySummary')
]
