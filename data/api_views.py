from rest_framework.generics import ListAPIView
from .serializers import DistrictWiseSerializer, Last24HoursSerializer, TotalSerializer
from .models import DistrictWise, Last24Hours, Total


class Last24HoursList(ListAPIView):
    """
    Get latest details from the last 24 hours
    """
    queryset = Last24Hours.objects.all()
    serializer_class = Last24HoursSerializer


class TotalList(ListAPIView):
    """
    Get total details since January 2020
    """
    queryset = Total.objects.all()
    serializer_class = TotalSerializer

class DistrictWiseList(ListAPIView):
    """
    Get detailed counts district-wise
    """
    queryset = DistrictWise.objects.all()
    serializer_class = DistrictWiseSerializer