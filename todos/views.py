# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse

from django.shortcuts import render
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()[:10]

    # return HttpResponse('Hello World!')
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)