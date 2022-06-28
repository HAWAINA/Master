from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    CalendarRegistration,
    CalendarRefactor,
    EmployeeCreation,
    EmployeeRefactor,
)
from .serializers import (
    CalendarRegistrationSerializer,
    CalendarRefactorSerializer,
    EmployeeRefactorSerializer,
    EmployeeCreationSerializer,
)


# Запросы насчёт создание сотрудника
@api_view(["GET", "POST"])
def employee_creation_view(request):
    try:
        employee_creation = EmployeeCreation.objects.all()
    except EmployeeCreation.DoesNotExist:
        return Response(
            data={"error": "Employee not Created!!!"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    if request.method == "GET":
        serializer = EmployeeCreationSerializer(employee_creation, many=True)
        return Response(data=serializer.data)
    elif request.method == "POST":
        profile = request.data.get("profile")
        nickname = request.data.get("nickname")
        tel_number = request.data.get("tel_number")
        service_specialty = request.data.get("service_specialty")
        length_of_service = request.data.get("length_of_service")
        calendar_register = request.data.get("calendars")
        employee_create = request.data.create(
            calendar_register=calendar_register,
            profile=profile,
            nickname=nickname,
            tel_number=tel_number,
            service_specialty=service_specialty,
            length_of_service=length_of_service,
        )
        return Response(data=EmployeeCreationSerializer(employee_create).data)


@api_view(["GET", "POST"])
def calendar_registration_view(request):
    try:
        calendar_registration = CalendarRegistration.objects.all()
    except CalendarRegistration.DoesNotExist:
        return Response(
            data={"error": "Calendar not Created!!!"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    if request.method == "GET":
        serializer = CalendarRegistrationSerializer(calendar_registration, many=True)
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
        return Response(data=CalendarRegistrationSerializer(calendar_create).data)


# Запросы по редактирование мастера
@api_view(["GET", "PUT", "DELETE"])
def employee_refactor_view(request, id):
    try:
        employee_refactor = EmployeeRefactor.objects.get(id=id)
    except EmployeeRefactor.DoesNotExist:
        return Response(
            data={"error": "Employee not Found!!!"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serializer = CalendarRefactorSerializer(employee_refactor)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        employee_refactor.delete()
        return Response(data={"massage": "Employee removed!"})
    else:
        employee_refactor.profile_ref = request.data.get("profile_ref")
        employee_refactor.nickname_ref = request.data.get("nickname_ref")
        employee_refactor.tel_number_ref = request.data.get("tel_number_ref")
        employee_refactor.service_specialty_ref = request.data.get("service_specialty_ref")
        employee_refactor.length_of_service_ref = request.data.get("length_of_service_ref")
        employee_refactor.description_ref = request.data.get("description_ref")
        employee_refactor.save()
        return Response(data=EmployeeRefactorSerializer(employee_refactor).data)


@api_view(["GET", "PUT", "DELETE"])
def calendar_refactor_view(request):
    try:
        calendar_refactor = CalendarRefactor.objects.get(id=id)
    except CalendarRefactor.DoesNotExist:
        return Response(
            data={"error": "Calendar not Found!!!"}, status=status.HTTP_404_NOT_FOUND
        )
    if request.method == "GET":
        serializer = CalendarRefactorSerializer(calendar_refactor)
        return Response(data=serializer.data)
    elif request.method == "DELETE":
        calendar_refactor.delete()
        return Response(data={"massage": "Calendar removed!"})
    else:
        calendar_refactor.work_calendar_ref = request.data.get("work_calendar_ref")
        calendar_refactor.getting_started_ref = request.data.get("getting_started_ref")
        calendar_refactor.end_of_job_ref = request.data.get("end_of_job_ref")
        calendar_refactor.lunch_start_ref = request.data.get("lunch_start_ref")
        calendar_refactor.lunch_end_ref = request.data.get("lunch_end_ref")
        calendar_refactor.save()
        return Response(data=CalendarRefactorSerializer(calendar_refactor).data)
