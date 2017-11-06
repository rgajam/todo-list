# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Todo

# Create your views here.
def hello(request):
    return HttpResponse('Hello World!')

def index(request):
    todos = Todo.objects.all()[:10]

    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def details(request, id):
    todo = Todo.objects.get(id=id)

    context = {
        'todo': todo
    }
    return render(request, 'details.html', context)
