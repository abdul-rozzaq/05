from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    year = models.IntegerField()
    color = models.CharField(max_length=256)
    price = models.IntegerField()
    max_speed = models.IntegerField()
    is_available = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.brand} {self.model} - {self.year}"


class Animal(models.Model):
    species = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    color = models.CharField(max_length=256)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.species}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
