from django.contrib import admin

from .models import CustomUser

from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdim(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model  = CustomUser
    list_display = ('username','email', 'age', 'is_staff', )

admin.site.register(CustomUser, CustomUserAdim)
