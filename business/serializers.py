from rest_framework import serializers
from . import models


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Calendar
        fields = "work_calendar getting_started end_of_job lunch_start lunch_end".split()
