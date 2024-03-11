from django.shortcuts import render
from django.views.generic import TemplateView

class UserPageView(TemplateView):
    template_name = 'userpage.html'

