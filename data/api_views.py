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
            cases = cases.filter(
                date_updated__startswith=request.GET.get("date"))

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

    def list(self, request):
        cases = Total.objects.order_by("-date_updated")

        if "date" in request.GET:
            cases = cases.filter(
                date_updated__startswith=request.GET.get("date"))

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

    def list(self, request):
        cases = Area.objects.order_by("-date_updated")

        if "date" in request.GET:
            cases = cases.filter(
                date_updated__startswith=request.GET.get("date"))

        if "district" in request.GET:
            print(request.GET.get("district").upper())
            cases = cases.filter(district=request.GET.get("district").upper())
            print(cases)

        if "gender" in request.GET:
            serializer = (
                AreaMaleSerializer(cases, many=True)
                if request.GET.get("gender") == "male"
                else AreaFemaleSerializer(cases, many=True)
            )
        else:
            serializer = AreaSerializer(cases, many=True)

        return Response(serializer.data)
