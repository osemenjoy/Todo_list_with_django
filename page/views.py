from django.shortcuts import render
from django.views.generic import ListView 
from .models import Task

class UserPageView(ListView):
    model = Task
    template_name = 'userpage.html'



