from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from business.models import EmployeeCreation, CalendarRegistration


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

    def velidate_employee_id(self, employee_id):
        if EmployeeCreation.objects.filter(id=employee_id).count() == 0:
            raise ValidationError(f"Employee with id={employee_id} not found!")
        return employee_id
