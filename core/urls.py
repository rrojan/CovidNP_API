from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from data.views import scrape_view
from pages import views as pages
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    # docs
    path("", pages.index_view, name="index"),
    path("docs/", pages.docs_view, name="docs"),
    path("changelogs/", pages.changelogs_view, name="changelogs"),
    # auth
    path("login/", pages.login, name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="pages/logout.html"), name="logout"
    ),
    path("signup", pages.signup_view, name="signup"),
    # my API
    path("my-api/", pages.my_api_view, name="my_api"),
    # API
    path("api/", include("api.urls")),
    # manual scraper
    path("scrape/", scrape_view, name="scrape"),
]
