from datetime import date
import time
from django.db import models
from django.utils import formats


CATEGORIES = ((1, "Last 24 Hours"), (2, "Total"), (3, "By District"))


class Daily(models.Model):
    new_cases = models.IntegerField()
    male_cases_estimated = models.IntegerField(null=True)
    female_cases_estimated = models.IntegerField(null=True)
    recovered = models.IntegerField()
    deaths = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=CATEGORIES, default=1)

    class Meta:
        verbose_name_plural = "Dailies"


class Total(models.Model):
    total_cases = models.IntegerField()
    total_infected = models.IntegerField()
    total_male_estimated = models.IntegerField(null=True)
    total_female_estimated = models.IntegerField(null=True)
    recovered = models.IntegerField()
    deaths = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=CATEGORIES, default=2)


def display_str(self):
    return (
        f"{self.get_category_display()} ["
        + formats.localize_input(self.date_updated)
        + "]"
    )


Daily.__str__ = Total.__str__ = display_str


class DistrictWise(models.Model):
    district = models.CharField(max_length=20)
    total_cases = models.IntegerField()
    total_male = models.IntegerField()
    total_female = models.IntegerField()
    daily_cases_estimated = models.IntegerField(null=True)
    daily_male_estimated = models.IntegerField(null=True)
    daily_female_estimated = models.IntegerField(null=True)
    date_updated = models.DateField(auto_now_add=True, null=True)
    category = models.IntegerField(choices=CATEGORIES, default=3)

    def __str__(self):
        return (
            f"{self.district} ["
            + formats.localize_input(self.date_updated)
            + "]"
        )
