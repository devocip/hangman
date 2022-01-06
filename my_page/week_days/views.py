from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

day_dict = {
    'monday': "Список дел на понедельник",
    'tuesday': "Список дел на вторник",
    'wednesday': "Список дел на среда",
    'thursday': "Список дел на четверг",
    'friday': "Список дел на пятница",
    'saturday': "Список дел на суббота",
    'sunday': "Список дел на воскресенье",
}


def get_day(request, day: str):
    description = day_dict.get(day, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Неизвестный день недели - {day}')


def get_day_by_number(request, day: int):
    spisok_days = list(day_dict)
    name_days = spisok_days[day - 1]
    if 1 <= day <= 7:
        redirect_urls = reverse('name_day', args=(name_days,))
        return HttpResponseRedirect(redirect_urls)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {day}')
