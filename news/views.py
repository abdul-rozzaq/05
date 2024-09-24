from django.shortcuts import render

def cars_page(request):
    return render(request, 'cars.html')


def animals_page(request):
    return render(request, 'animals.html')

