from rest_framework import serializers

from .models import Last24Hours, Total, DistrictWise


class Last24HoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Last24Hours
        fields = ("new_cases", "recovered", "deaths", "date_updated")


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = (
            "total_cases",
            "total_infected",
            "recovered",
            "deaths",
            "date_updated",
        )


class DistrictWiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictWise
        fields = (
            "district",
            "total_cases",
            "total_male",
            "total_female",
            "daily_cases_estimated",
            "daily_male_estimated",
            "daily_female_estimated",
            "date_updated",
        )
