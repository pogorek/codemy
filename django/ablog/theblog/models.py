from django.db import models
# thats the superuser we created
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date


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


class Post(models.Model):
    title = models.CharField(max_length=255)  # , default="My Awesome Blog")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    # dodajemy date , problem z utworzonymi wczesniej postami w konsoli 1 i enter, w video DateField
    post_date = models.DateTimeField(auto_now_add=True)
    # category = models.CharField(max_length=255, default="unknown")
    category = models.ForeignKey(
        Category, max_length=60, on_delete=models.CASCADE, related_name='catego')

    def __str__(self):
        return f"{self.title} | {self.author}"

    # nie potrzeba w html wpisywac action="", tutaj okreslamy co ma sie stac
    def get_absolute_url(self):
        # to przekierowuje na strone artykulu, dodaje argument
        # return reverse("article_detail", args=(str(self.id)))
        return reverse("home")
