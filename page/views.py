from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Task
from django.urls import  reverse_lazy


class UserCreateView(CreateView, ListView):
    model = Task
    template_name = 'userpage.html'
    fields = {'task_name'}
    success_url = reverse_lazy('userpage')

    