from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import (
    DailySerializer,
    DailyMaleSerializer,
    DailyFemaleSerializer,
    TotalSerializer,
    TotalMaleSerializer,
    TotalFemaleSerializer,
    AreaSerializer,
    AreaMaleSerializer,
    AreaFemaleSerializer,
)
from .models import Area, Daily, Total
from . import nepal_data

# TODO: use drf filter lib instead of manually filtering url queries


class DailyList(ViewSet):
    """
    Get latest details from the last 24 hours
    """

    # QUERY_FIELDS = [
    #     "date",
    #     "gender",
    # ]

    def list(self, request):
        cases = Daily.objects.order_by("-date_updated")

        if "date" in request.GET:
            cases = cases.filter(date_updated__startswith=request.GET.get("date"))

        if "gender" in request.GET:
            serializer = (
                DailyMaleSerializer(cases, many=True)
                if request.GET.get("gender") == "male"
                else DailyFemaleSerializer(cases, many=True)
            )
        else:
            serializer = DailySerializer(cases, many=True)

        return Response(serializer.data)


class TotalList(ViewSet):
    """
    Get total details since January 2020
    """

    # QUERY_FIELDS = [
    #     "date",
    #     "gender",
    # ]

    def list(self, request):
        cases = Total.objects.order_by("-date_updated")

        if "date" in request.GET:
            cases = cases.filter(date_updated__startswith=request.GET.get("date"))

        if "gender" in request.GET:
            serializer = (
                TotalMaleSerializer(cases, many=True)
                if request.GET.get("gender") == "male"
                else TotalFemaleSerializer(cases, many=True)
            )
        else:
            serializer = TotalSerializer(cases, many=True)

        return Response(serializer.data)


class AreaList(ViewSet):
    # QUERY_FIELDS = [
    #     "province",
    #     "district",
    #     "date",
    #     "gender",
    # ]

    """
    Get detailed counts district-wise
    """

    def get_province_cases(self, province):
        province = province.lower()
        if province in nepal_data.PROVINCES.keys():
            province_cases = list()
            for district in nepal_data.PROVINCES[province]:
                district_cases = list(Area.objects.filter(district=district))
                province_cases += district_cases
            return province_cases

    def list(self, request):
        cases = Area.objects.order_by("-date_updated")

        if "date" in request.GET:
            cases = cases.filter(date_updated__startswith=request.GET.get("date"))

        if "district" in request.GET:
            cases = cases.filter(district=request.GET.get("district").upper())

        if "province" in request.GET:
            cases = self.get_province_cases(request.GET.get("province"))

        if "gender" in request.GET:
            serializer = (
                AreaMaleSerializer(cases, many=True)
                if request.GET.get("gender") == "male"
                else AreaFemaleSerializer(cases, many=True)
            )
        else:
            serializer = AreaSerializer(cases, many=True)

        return Response(serializer.data)
