from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm


# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
    # LOGIN_REDIRECT_URL = 'home' w settings.py


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm  # UserChangeForm / przed update
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")
    # LOGIN_REDIRECT_URL = 'home' w settings.py

    # function will return current user
    def get_object(self):
        return self.request.user
