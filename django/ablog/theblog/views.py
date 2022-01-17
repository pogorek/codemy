import re
from django.shortcuts import render
# for CBV
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    # zmienia kolejnosc postow od najwiekszego id
    # ordering = ["-id"]
    # zmienia kolejnosc postow od najnowszej daty
    ordering = ["-post_date"]


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # przez uzycie PostForm nie dodajemy fields
    # fields = "__all__"
    # nie trzeba wszystkich fields, mozna wybrac, moga byc () lub []
    # fields = ("title", "author", "body")


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    # fields = ["title", "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    # gdy uda sie usunac to tutaj okreslamy gdzie przekierowac, zwykle reverse nie dziala
    success_url = reverse_lazy("home")
