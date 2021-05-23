from rest_framework import serializers

from .models import Daily, Total, Area


class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = Daily


class DailySerializer(DailySerializer):
    class Meta(DailySerializer.Meta):
        fields = (
            "new_cases",
            "male_cases_estimated",
            "female_cases_estimated",
            "recovered",
            "deaths",
            "date_updated",
            "source",
        )


class DailyMaleSerializer(DailySerializer):
    class Meta(DailySerializer.Meta):
        fields = ("male_cases_estimated", "date_updated", "source")


class DailyFemaleSerializer(DailySerializer):
    class Meta(DailySerializer.Meta):
        fields = ("female_cases_estimated", "date_updated", "source")


class TotalBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total


class TotalSerializer(TotalBaseSerializer):
    class Meta(TotalBaseSerializer.Meta):
        fields = (
            "total_cases",
            "total_infected",
            "total_male_estimated",
            "total_female_estimated",
            "recovered",
            "deaths",
            "date_updated",
            "source",
        )


class TotalMaleSerializer(TotalBaseSerializer):
    class Meta(TotalBaseSerializer.Meta):
        fields = ("total_male_estimated", "date_updated", "source")


class TotalFemaleSerializer(TotalBaseSerializer):
    class Meta(TotalBaseSerializer.Meta):
        fields = ("total_female_estimated", "date_updated", "source")


class AreaBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area


class AreaSerializer(AreaBaseSerializer):
    class Meta(AreaBaseSerializer.Meta):
        fields = (
            "district",
            "total_cases",
            "total_male",
            "total_female",
            "daily_cases_estimated",
            "daily_male_estimated",
            "daily_female_estimated",
            "date_updated",
            "source",
        )


class AreaMaleSerializer(AreaBaseSerializer):
    class Meta(AreaBaseSerializer.Meta):
        fields = ("total_male", "daily_male_estimated", "date_updated", "source")


class AreaFemaleSerializer(AreaBaseSerializer):
    class Meta(AreaBaseSerializer.Meta):
        fields = ("total_female", "daily_female_estimated", "date_updated", "source")
