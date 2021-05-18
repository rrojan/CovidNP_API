from django.urls import path, include
from data import api_views as data

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("last-24-hours/", data.Last24HoursList.as_view(), name="last_24_hours"),
    path("total/", data.TotalList.as_view(), name="total"),
    path("district/", data.DistrictWiseList.as_view(), name="district_wise"),
]
