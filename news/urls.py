
from django.urls import path

from .views import cars_page

urlpatterns = [
    path('', cars_page, name='cars_page')
]