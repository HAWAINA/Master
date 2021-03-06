from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Calendar,
    Employee,
)
from .serializers import (
    CalendarSerializer,
    EmployeeSerializer,
)


@api_view(["GET", "POST"])
def employee_view(request):
    try:
        employee = Employee.objects.all()
    except Employee.DoesNotExist:
        return Response(
            data={"error": "Employee not Created!!!"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    if request.method == "GET":
        serializer = EmployeeSerializer(employee, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        profile = request.data.get("profile")
        nickname = request.data.get("nickname")
        tel_number = request.data.get("tel_number")
        service_specialty = request.data.get("service_specialty")
        length_of_service = request.data.get("length_of_service")
        description = request.data.get("description")
        calendar_register = request.data.get("calendar_register")
        employee_create = Employee.objects.create(
            profile=profile,
            nickname=nickname,
            tel_number=tel_number,
            service_specialty=service_specialty,
            length_of_service=length_of_service,
            description=description,
            calendar_register=calendar_register,
        )
        return Response(data=EmployeeSerializer(employee_create).data)


@api_view(["GET", "PUT", "DELETE"])
def employee_refactor_view(request, id):
    try:
        employee_create = Employee.objects.all().filter(id=id)
    except Employee.DoesNotExist:
        return Response(
            data={"error": "Employee not Found!!!"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serializer = EmployeeSerializer(employee_create, many=True)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        employee_create.delete()
        return Response(data={"massage": "Employee removed!"})
    else:
        employee_create.profile = request.data.get("profile")
        employee_create.nickname = request.data.get("nickname")
        employee_create.tel_number = request.data.get("tel_number")
        employee_create.service_specialty = request.data.get("service_specialty")
        employee_create.length_of_service = request.data.get("length_of_service")
        employee_create.description = request.data.get("description")
        employee_create.description = request.data.get("description")
        employee_create.calendar_register = request.data.get("calendar_register")
        employee_create.save()
        return Response(data=EmployeeSerializer(employee_create).data)


@api_view(["GET", "POST"])
def calendar_view(request):
    try:
        calendar = Calendar.objects.all().filter(id=id)
    except Calendar.DoesNotExist:
        return Response(
            data={"error": "Calendar not Created!!!"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    if request.method == "GET":
        serializer = CalendarSerializer(calendar, many=True)
        return Response(data=serializer.data)
    if request.method == "POST":
        work_calendar = request.data.get("work_calendar")
        getting_started = request.data.get("getting_started")
        end_of_job = request.data.get("end_of_job")
        lunch_start = request.data.get("lunch_start")
        lunch_end = request.data.get("lunch_end")
        calendar_create = request.data.create(
            work_calendar=work_calendar,
            getting_started=getting_started,
            end_of_job=end_of_job,
            lunch_start=lunch_start,
            lunch_end=lunch_end,
        )
        return Response(data=CalendarSerializer(calendar_create).data)


@api_view(["GET", "PUT", "DELETE"])
def calendar_refactor_view(request):
    try:
        calendar = Calendar.objects.get(id=id)
    except Calendar.DoesNotExist:
        return Response(
            data={"error": "Calendar not Found!!!"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serializer = CalendarSerializer(calendar)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        calendar.delete()
        return Response(data={"massage": "Calendar removed!"})
    else:
        calendar.work_calendar = request.data.get("work_calendar")
        calendar.getting_started = request.data.get("getting_started")
        calendar.end_of_job = request.data.get("end_of_job")
        calendar.lunch_start = request.data.get("lunch_start")
        calendar.lunch_end = request.data.get("lunch_end")
        calendar.save()
        return Response(data=CalendarSerializer(calendar).data)
