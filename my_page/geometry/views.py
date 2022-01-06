from django.http import HttpResponse, HttpResponseRedirect

from math import *

# Create your views here.

def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}х{height} равна {width * height}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}х{width} равна {width * width}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {pi * (radius ** 2)} ')

