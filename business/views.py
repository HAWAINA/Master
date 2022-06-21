from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CalendarRegistration, CalendarRefactor, EmployeeCreation, EmployeeRefactor
from .serializers import CalendarSerializer, CalendarRefactorSerializer, \
    EmployeeRefactorSerializer


# Запросы насчёт создание сотрудника
@api_view(["POST", "GET"])
def EmployeeCreationView(request):
    employee_creation = EmployeeCreation.objects.all()
    data = CalendarSerializer(employee_creation, many=True).data
    return Response(data=data)


@api_view(["POST", "GET"])
def CalendarRegistrationView(request):
    calendar = CalendarRegistration.objects.all()
    data = CalendarSerializer(calendar, many=True).data
    return Response(data=data)


# Запросы по редактирование мастера
@api_view(["PUT"])
def EmployeeRefactorView(request):
    employee_ref = EmployeeRefactor.objects.all()
    data = EmployeeRefactorSerializer(employee_ref, many=True).data
    return Response(data=data)


@api_view(["PUT"])
def CalendarRefactorView(request):
    calendar_ref = CalendarRefactor.objects.all()
    data = CalendarRefactorSerializer(calendar_ref, many=True).data
    return Response(data=data)
