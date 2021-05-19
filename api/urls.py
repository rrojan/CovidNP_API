from django.urls import path, include
from rest_framework import routers
from data import api_views as data
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"daily", data.DailyList, basename="last_24_hours")
router.register(r"total", data.TotalList, basename="total")
router.register(r"area", data.AreaList, basename="district_wise")

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls)),
]
