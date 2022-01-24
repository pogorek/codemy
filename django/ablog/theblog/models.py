from django.db import models
# thats the superuser we created
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# trzeba dodac do settings.py - installed apps - 'ckeditor', a w .html - {{ form.media }}
from ckeditor.fields import RichTextField


# Create your models here.
class Category(models.Model):
    # by w admin nie bylo Categorys , poprawia liczbe mnoga
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    # nie potrzeba w html wpisywac action="", tutaj okreslamy co ma sie stac
    def get_absolute_url(self):
        # to przekierowuje na strone artykulu, dodaje argument
        # return reverse("article_detail", args=(str(self.id)))
        return reverse("home")


# rozwiniecie profilu uzytkownika
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, null=True, blank=True)
    fb_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        # to przekierowuje na strone artykulu, dodaje argument
        # return reverse("article_detail", args=(str(self.id)))
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=255)  # , default="My Awesome Blog")
    header_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # wersja bez RichTextField
    # body = models.TextField()
    # dodajemy date , problem z utworzonymi wczesniej postami w konsoli 1 i enter, w video DateField
    post_date = models.DateTimeField(auto_now_add=True)
    # category = models.CharField(max_length=255, default="unknown")
    category = models.ForeignKey(
        Category, max_length=60, on_delete=models.CASCADE, related_name='catego')
    likes = models.ManyToManyField(User, related_name="blog_posts")
    # usuwamy default po piejwszej migrate by w starych postach wypelnilo sie to pole
    snippet = models.CharField(max_length=255)  # , default="Old Post")

    def __str__(self):
        return f"{self.title} | {self.author}"

    # nie potrzeba w html wpisywac action="", tutaj okreslamy co ma sie stac
    def get_absolute_url(self):
        # to przekierowuje na strone artykulu, dodaje argument
        # return reverse("article_detail", args=(str(self.id)))
        return reverse("home")

    # zwraca likcze polubien posta
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.post.title, self.name)
