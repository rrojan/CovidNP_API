from rest_framework import serializers

from .models import Last24Hours, Total


class Last24HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Last24Hours
        fields = ("new_cases", "recovered", "deaths", "date_updated")


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = ("total_cases", "total_infected", "recovered", "deaths", "date_updated")
