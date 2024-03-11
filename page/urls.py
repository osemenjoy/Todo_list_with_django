from django.urls import path
from .views import UserPageView

urlpatterns = [
    path('your/',UserPageView.as_view(),name='userpage'),
]