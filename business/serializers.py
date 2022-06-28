from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from business.models import EmployeeCreation, CalendarRegistration, EmployeeRefactor, CalendarRefactor


# Создание сотрудника:
class CalendarRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarRegistration
        fields = (
            "work_calendar getting_started end_of_job lunch_start lunch_end".split()
        )


class EmployeeCreationSerializer(serializers.ModelSerializer):
    calendar_register = CalendarRegistrationSerializer()

    class Meta:
        model = EmployeeCreation
        fields = "id profile nickname tel_number service_specialty length_of_service calendar_register " \
                 "calendar_register".split()


# Редактирование сотрудника:
class CalendarRefactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarRefactor
        fields = "work_calendar_ref getting_started_ref end_of_job_ref lunch_start_ref lunch_end_ref".split()


class EmployeeRefactorSerializer(serializers.ModelSerializer):
    # calendar_ref = CalendarRefactorSerializer()

    class Meta:
        model = EmployeeRefactor
        fields = "id profile_ref nickname_ref tel_number_ref service_specialty_ref length_of_service_ref " \
                 "description_ref".split()

    def velidate_employee_id(self, employee_id):
        if EmployeeCreation.objects.filter(id=employee_id).count() == 0:
            raise ValidationError(f"Employee with id={employee_id} not found!")
        return employee_id
