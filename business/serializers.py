from rest_framework import serializers
from . import models


# Создание сотрудника:
class CalendarRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CalendarRegistration
        fields = (
            "work_calendar getting_started end_of_job lunch_start lunch_end".split()
        )


class EmployeeCreationSerializer(serializers.ModelSerializer):
    calendar_registration = CalendarRegistrationSerializer()

    class Meta:
        model = models.EmployeeCreation
        fields = "profile nickname tel_number service_specialty length_of_service calendar_registration"


# Редактирование сотрудника:
class CalendarRefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CalendarRefactor
        fields = "work_calendar_ref getting_started_ref end_of_job_ref lunch_start_ref lunch_end_ref"


class EmployeeRefactorSerializer(serializers.ModelSerializer):
    calendar_ref = CalendarRefactorSerializer()

    class Meta:
        model = models.EmployeeRefactor
        fields = "profile_ref nickname_ref tel_number_ref service_specialty_ref length_of_service_ref description_ref calendar_ref"
