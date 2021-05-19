from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Daily, Total, Area
from scraper import scrape
from datetime import date


def scrape_view(request):
    """
    Scrape but store only one database entry per day.

    If multiple scrapings are done in one day, remove all previous db entries for the day
    before creating the new object
    """

    url = "https://covid19.mohp.gov.np/"

    today_data, total_data, district_wise_data = scrape(url)

    old_objects = Daily.objects.filter(date_updated__startswith=date.today())
    for object in old_objects:
        object.delete()

    Daily.objects.create(
        new_cases=today_data["New Cases"],
        recovered=today_data["Recovered"],
        deaths=today_data["Deaths"],
    )

    old_objects = Total.objects.filter(date_updated__startswith=date.today())
    for object in old_objects:
        object.delete()

    Total.objects.create(
        total_cases=total_data["Total Cases"],
        total_infected=total_data["Total Infected"],
        recovered=total_data["Recovered"],
        deaths=total_data["Deaths"],
    )

    old_objects = Area.objects.filter(date_updated__startswith=date.today())
    for object in old_objects:
        object.delete()

    for data in district_wise_data:
        Area.objects.create(
            district=data["District"],
            total_cases=data["Total"],
            total_male=data["Male"],
            total_female=data["Female"],
        )

    return HttpResponse("Successfully scraped that shit")
