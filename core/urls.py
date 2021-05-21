from data.views import scrape_view
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from pages import views as pages
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", pages.index_view, name="index"),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='pages/logout.html'), name='logout'),
    # path('signup', pages.signup_view, name='signup'),
    path("docs/", pages.docs_view, name="docs"),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("scrape/", scrape_view, name="scrape"),
]
