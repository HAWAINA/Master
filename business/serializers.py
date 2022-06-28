from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from business.models import Employee, Calendar


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = (
            "work_calendar getting_started end_of_job lunch_start lunch_end".split()
        )


class EmployeeSerializer(serializers.ModelSerializer):
    calendar_register = CalendarSerializer()

    class Meta:
        model = Employee
        fields = "id profile nickname tel_number service_specialty length_of_service calendar_register " \
                 "calendar_register".split()

    def velidate_employee_id(self, employee_id):
        if Employee.objects.filter(id=employee_id).count() == 0:
            raise ValidationError(f"Employee with id={employee_id} not found!")
        return employee_id
