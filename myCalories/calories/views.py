from django.shortcuts import render
from .managers import *


# Create your views here.


def main_view(request):
    User.drop_collection()
    add_new_user('Lukas@root.pl', 'Lukas', 'Ptak', 165, 60, 21)
    print(get_user('Lukas@root.pl'))
    return render(request, "index.html", {})
