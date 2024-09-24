from django import forms

from .models import Animal, Book, Car, Movie, Student


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = "__all__"


class BookForm(forms.ModelForm):
    published_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    
    class Meta:
        model = Book
        fields = "__all__"


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class MovieForm(forms.ModelForm):
    release_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))

    class Meta:
        model = Movie
        fields = "__all__"


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
