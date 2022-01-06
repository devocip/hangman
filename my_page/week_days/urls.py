from django.urls import path

from week_days import views

urlpatterns = [
    path('<int:day>', views.get_day_by_number),
    path('<str:day>', views.get_day, name='name_day'),
    ]

