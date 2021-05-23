from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from data.views import scrape_view
from pages import views as pages
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    ###
    # docs
    path("", pages.index_view, name="index"),
    path("docs/", pages.docs_view, name="docs"),
    path("changelogs/", pages.changelogs_view, name="changelogs"),
    ###
    # auth
    path("login/", pages.login, name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="pages/logout.html"), name="logout"
    ),
    path("signup", pages.signup_view, name="signup"),
    ###
    # password reset routes
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="pages/password_reset/password_reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="pages/password_reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="pages/password_reset/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="pages/password_reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    ###
    # my API
    path("my-api/", pages.my_api_view, name="my_api"),
    ###
    # API
    path("api/", include("api.urls")),
    ###
    # automated scraper
    path("scrape/", scrape_view, name="scrape"),
]
