from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        "all_courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('')
    else:
    # if request.method=='POST':
        new_course = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
        return redirect('') 
    # return redirect('')

