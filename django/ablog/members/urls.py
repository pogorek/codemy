from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView
# for using ready vievs from auth django, later we created our own view
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    # using default django view to activate change-password option
    # then with template name changing default page to our template
    # v1 but after changing pass we want to redirect to HOME so we created new view below
    # path("password/", auth_views.PasswordChangeView.as_view(
    #     template_name="registration/change-password.html"), name="change_password"),
    path("password/", PasswordsChangeView.as_view(
        template_name="registration/change-password.html"), name="change_password"),
    path("password_success/", views.password_success, name="password_success"),
    path("<int:pk>/profile/", ShowProfilePageView.as_view(),
         name="show_profile_page"),

]
