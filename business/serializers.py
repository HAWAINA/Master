from rest_framework import serializers
from . import models


# Создание сотрудника:
class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployeeRegistration
        fields = "__all__"


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Calendar
        fields = "work_calendar getting_started end_of_job lunch_start lunch_end".split()


class EmployeeCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployeeCreation
        fields = "__all__"


# Редактирование сотрудника:
class CalendarRefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CalendarRefactor
        fields = "work_calendar_ref getting_started_ref end_of_job_ref lunch_start_ref lunch_end_ref"


class EmployeeRefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployeeRefactor
        fields = "__all__"
