from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Calendar, CalendarRefactor, EmployeeCreation
from .serializers import CalendarSerializer, CalendarRefactorSerializer


@api_view(["POST", "GET"])
def CalendarView(request):
    calendar = Calendar.objects.all()
    data = CalendarSerializer(calendar, many=True).data
    return Response(data=data)


@api_view(["PATCH"])
def CalendarRefactorView(request):
    calendar_ref = CalendarRefactor.objects.all()
    data = CalendarRefactorSerializer(calendar_ref, many=True).data
    return Response(data=data)


@api_view(["POST", "GET"])
def EmployeeCreationView(request):
    employee_creation = EmployeeCreation.objects.all()
    data = CalendarSerializer(employee_creation, many=True).data
    return Response(data=data)
