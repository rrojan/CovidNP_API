from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Daily, Total, Area
from scraper import scrape
from datetime import date, timedelta


def scrape_view(request):
    """
    Scrape but store only one database entry per day.

    If multiple scrapings are done in one day, remove all previous db entries for the day
    before creating the new object.

    The url route for this view will be triggered periodically using cronjobs by running a curl request containing
    a check string.
    e.g. curl -X GET http://127.0.0.1:8000/scrape/?passphrase=test

    It can also be done manually by an authorized user.
    """

    print(request.GET.get("passphrase"))
    if request.GET.get("passphrase") != "test":
        return redirect("index")

    url = "https://covid19.mohp.gov.np/"

    today_data, total_data, district_wise_data = scrape(url)

    # The district wise data element in the mohp site is slow to load so sometimes it might not return anything

    # There might still be an earlier scrape in the same day that has already saved them in the db,
    # so check if the scrape returned any new data before deleting previous rows
    if district_wise_data:
        old_objects = Area.objects.filter(date_updated__startswith=date.today())
        for object in old_objects:
            object.delete()

    total_male_count = total_female_count = 0

    for data in district_wise_data:
        Area.objects.create(
            district=data["District"],
            total_cases=data["Total"],
            total_male=data["Male"],
            total_female=data["Female"],
        )

        # calculate total male and female count for Total instance
        total_male_count += data["Male"]
        total_female_count += data["Female"]

    old_objects = Total.objects.filter(date_updated__startswith=date.today())
    for object in old_objects:
        object.delete()
    
    try:
        yesterday_date = date.today() - timedelta(days=1)
        print(yesterday_date)
        yst_total = Total.objects.get(
            date_updated__startswith=yesterday_date
        )
        yst_total_male_count = yst_total.total_male_estimated
        yst_total_female_count = yst_total.total_female_estimated
        daily_male_count = total_male_count - yst_total_male_count
        daily_female_count = total_female_count - yst_total_female_count
    except Exception:
        daily_male_count = None
        daily_female_count = None

    Total.objects.create(
        total_cases=total_data["Total Cases"],
        total_infected=total_data["Total Infected"],
        recovered=total_data["Recovered"],
        deaths=total_data["Deaths"],
        total_male_estimated=total_male_count,
        total_female_estimated=total_female_count,
    )

    old_objects = Daily.objects.filter(date_updated__startswith=date.today())
    for object in old_objects:
        object.delete()

    

    Daily.objects.create(
        new_cases=today_data["New Cases"],
        recovered=today_data["Recovered"],
        deaths=today_data["Deaths"],
        male_cases_estimated=daily_male_count,
        female_cases_estimated=daily_female_count,
    )

    return HttpResponse("Successfully scraped data from target")
