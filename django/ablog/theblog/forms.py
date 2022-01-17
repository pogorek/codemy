from django import forms
from .models import Post


# clasa dodajaca atrybuty do pol
class PostForm(forms.ModelForm):
    class Meta:
        # w jakim modelu ma dodac atrybuty
        model = Post
        # jakie pola maja byc w tej klasie
        fields = ("title", "title_tag", "author", "body")

        # dodaje atrybuty do pol okreslonych w modelu
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title goes here"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "body")

        # dodaje atrybuty do pol okreslonych w modelu
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title goes here"}),
            # "title_tag": forms.TextInput(attrs={"class": "form-control"}),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }
