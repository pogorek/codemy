import re
from django.shortcuts import render
# for CBV
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
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

    # przesyłanie argumentow jak w funkcji {"oko": oko}
    def get_context_data(self, *args, **kwargs):
        # zapytanie o wszystkie obiekty w klassie Category
        cat_menu = Category.objects.all()
        # ??
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        # ???
        context["cat_menu"] = cat_menu
        return context


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


class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    # tylko jedno pole, uzyjemy
    fields = "__all__"
    template_name = "add_category.html"


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


def CategoryView(request, cats):
    # zamieniamy myslnik na spacje
    cats = cats.replace('-', ' ')
    # wyciagamy id categorii
    categ_id = Category.objects.filter(name=cats)
    # if there are results
    if categ_id:
        categ_id = Category.objects.filter(name=cats)[0].id
        # filter(category=categ_id) - filtruje zapytanie tylko dla postow z okreslonym id kategorii
        category_posts = Post.objects.filter(category=categ_id)
    # if no results
    else:
        return render(request, "categories.html", {
            "cats": "No page",
        })

    return render(request, "categories.html", {
        "cats": cats.title(),
        # "categ_name": categ_name,
        "category_posts": category_posts,
    })

# funkcja pojawwiajaca sie gdy nie ma dropdown menu


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, "category_list.html", {
        "cat_menu_list": cat_menu_list,
    })
