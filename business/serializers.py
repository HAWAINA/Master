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
    calendar = CalendarSerializer()

    class Meta:
        model = Employee
        fields = "id profile nickname tel_number service_specialty length_of_service calendar calendar".split()

