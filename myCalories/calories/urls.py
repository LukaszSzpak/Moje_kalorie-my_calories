from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_view, name='index'),
    path('index', views.main_view, name='index'),
    path('sample', views.sample_data),
    path('post/ajax/dayFoodList', views.get_food_list, name='dayFoodList')
]
