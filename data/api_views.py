from rest_framework.generics import ListAPIView
from .serializers import Last24HoursSerializer, TotalSerializer
from .models import Last24Hours, Total


class Last24HoursList(ListAPIView):
    queryset = Last24Hours.objects.all()
    serializer_class = Last24HoursSerializer


class TotalList(ListAPIView):
    queryset = Total.objects.all()
    serializer_class = TotalSerializer
