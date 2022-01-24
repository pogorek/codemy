import re
# get_object_or_404 - get object and if id does not exist - 404
from django.shortcuts import render, get_object_or_404
# for CBV
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
# for LikeView
from django.http import HttpResponseRedirect


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

    # przesyłanie argumentow jak w funkcji {"oko": oko}
    def get_context_data(self, *args, **kwargs):
        # zapytanie o wszystkie obiekty w klassie Category
        cat_menu = Category.objects.all()
        # ??
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        # ???
        context["cat_menu"] = cat_menu

        # get from post table, a post with pk of post that page we are currently on
        temp = get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes = temp.total_likes()
        context["total_likes"] = total_likes

        # like/unlike
        liked = False
        if temp.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["liked"] = liked

        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm  # request.POST,request.FILES)
    template_name = "add_post.html"
    # przez uzycie PostForm nie dodajemy fields
    # fields = "__all__"
    # nie trzeba wszystkich fields, mozna wybrac, moga byc () lub []
    #fields = ("title", "body")

    # ustawia zalogowanego uzytkownika jako autora
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    #success_url = reverse_lazy("home")
    # przez uzycie PostForm nie dodajemy fields
    # fields = "__all__"
    # nie trzeba wszystkich fields, mozna wybrac, moga byc () lub []
    #fields = ("title", "body")

    # ustawia id posta z kwargs
    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)

    # przekierowuje na strone posta po dodaniu kommenta
    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.kwargs['pk']})


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


def LikeView(request, pk):
    # get id from form, check in post table which post it is, then assign it to post var
    # z komentow - post = Post.objects.get(id=pk)
    post = get_object_or_404(Post, id=request.POST.get("post_id"))

    liked = False
    # if already liked, after clicking, remove like - unlike
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        # save like to the table, from who it is
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse("article_detail", args=[str(pk)]))
