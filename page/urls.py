from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('your/',UserCreateView.as_view(),name='userpage'),
]