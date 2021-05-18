from django.db import models
from django.utils import formats


CATEGORIES = ((1, "Last 24 Hours"), (2, "Total"), (3, "By Province"))


class Last24Hours(models.Model):
    new_cases = models.IntegerField()
    recovered = models.IntegerField()
    deaths = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=CATEGORIES, default=1)

    class Meta:
        verbose_name_plural = "Last 24 hours"


class Total(models.Model):
    total_cases = models.IntegerField()
    total_infected = models.IntegerField()
    recovered = models.IntegerField()
    deaths = models.IntegerField()
    date_updated = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField(choices=CATEGORIES, default=2)


def display_str(self):
    return (
        f"{self.get_category_display()} ["
        + formats.date_format(self.date_updated, "SHORT_DATETIME_FORMAT")
        + "]"
    )


Last24Hours.__str__ = Total.__str__ = display_str
