from data.views import scrape_view
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from pages import views as pages


urlpatterns = [
    path("", pages.index_view, name="index"),
    path("docs/", pages.docs_view, name="docs"),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("scrape/", scrape_view, name="scrape"),
]
