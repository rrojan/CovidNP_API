from django.urls import path, include
from rest_framework import routers
from data import api_views as data
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r"last24hours", data.Last24HoursList, basename="last_24_hours")
router.register(r"total", data.TotalList, basename="total")
router.register(r"district", data.DistrictWiseList, basename="district_wise")

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("", include(router.urls)),
    # path("last-24-hours/", data.Last24HoursList.as_view(), name="last_24_hours"),
    # path("total/", data.TotalList.as_view(), name="total"),
    # path("district/", data.DistrictWiseList.as_view(), name="district_wise"),
]
