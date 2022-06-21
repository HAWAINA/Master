from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import models
from . import serializers
from .models import Calendar
from .serializers import CalendarSerializer


@api_view(["POST", "GET"])
def CalendarView(request):
    calendar = Calendar.objects.all()
    data = CalendarSerializer(calendar, many=True).data
    return Response(data=data)

