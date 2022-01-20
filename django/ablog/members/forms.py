from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


# tworzymy nowa klase na bazie UserCreationForm
class SignUpForm(UserCreationForm):
    # dodajemy atrybuty dla kazdego pola
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2")

    # funkcja, ktora doda argumenty do username, pass1 i pass2
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # dodajemy atrybuty do poszczegolnych pol
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"


class EditProfileForm(UserChangeForm):
    # dodajemy atrybuty dla kazdego pola
    # mozna sprawdzic id pol w kodzie zrodlowym strony
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    # nie używane
    # last_login = forms.CharField(
    #     max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    # is_superuser = forms.CharField(
    #     max_length=100, widget=forms.CheckboxInput(attrs={"class": "form-check"}))
    # is_staff = forms.CharField(
    #     max_length=100, widget=forms.CheckboxInput(attrs={"class": "form-check"}))
    # is_active = forms.CharField(
    #     max_length=100, widget=forms.CheckboxInput(attrs={"class": "form-check"}))
    # date_joined = forms.CharField(
    #     max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    # ukrywa password opis, ktory bez tego sie pojawia
    # password = None

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", )  # nie używane "password", "last_login", "is_superuser", "is_staff", "is_active", "date_joined")
