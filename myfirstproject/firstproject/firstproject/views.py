from django.shortcuts import render
from scripts import customscript

def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    name = request.GET['name']
    age = request.GET['age']
    num = customscript.multiplies(int(age))
    return render(request, 'result.html', {'name' : name, 'age':age, 'num':num})
