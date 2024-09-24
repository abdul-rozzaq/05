from django.shortcuts import render

from .models import Animal, Book, Car, Movie, Student
from .forms import CarForm, BookForm, AnimalForm, MovieForm, StudentForm

def cars_page(request):
    cars = Car.objects.all()
        
    if request.method == "POST":
        form = CarForm(request.POST)
        
        if form.is_valid():
            form.save()
            

    form = CarForm()
    
    return render(request, "cars.html", {'cars': cars, 'form': form})


def animals_page(request):
    animals = Animal.objects.all()
    
    if request.method == "POST":
        form = AnimalForm(request.POST)
        
        if form.is_valid():
            form.save()
            
    form = AnimalForm()
    
    return render(request, "animals.html", {'animals': animals, 'form': form})


def books_page(request):
    books = Book.objects.all()
    
    if request.method == "POST":
        form = BookForm(request.POST)
        
        if form.is_valid():
            form.save()
            
    form = BookForm()
    
    return render(request, "books.html", {'books': books, 'form': form})


def movies_page(request):
    movies = Movie.objects.all()
    
    if request.method == "POST":
        form = MovieForm(request.POST)
        
        if form.is_valid():
            form.save()

    form = MovieForm()

    return render(request, "movies.html", {'movies': movies, 'form': form})


def students_page(request):
    students = Student.objects.all()
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        
        if form.is_valid():
            form.save()
             
    form = StudentForm()
    
    return render(request, "students.html", {'students': students, 'form': form})
