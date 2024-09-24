
from django.urls import path

from .views import cars_page, animals_page, books_page, movies_page, students_page

urlpatterns = [
    path('', books_page, name='books_page'),
    path('animals/', animals_page, name='animals_page'),
    path('cars/', cars_page, name='cars_page'),
    path('movies/', movies_page, name='movies_page'),
    path('students/', students_page, name='students_page'),
]