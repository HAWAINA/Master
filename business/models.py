from django.db import models


# Создание сотрудника логика находится тут:
class CalendarRegistration(models.Model):
    work_calendar = models.DateField(verbose_name="Календарь", null=True)
    getting_started = models.TimeField(verbose_name="Начало Работы")
    end_of_job = models.TimeField(verbose_name="Конец Работы")
    lunch_start = models.TimeField(verbose_name="Начала обеда", null=True)
    lunch_end = models.TimeField(verbose_name="Конец обеда", null=True)

    class Meta:
        verbose_name = "Work Calendar"


class EmployeeCreation(models.Model):
    profile = models.ImageField(
        verbose_name="Профиль сотрудника", null=True
    )
    nickname = models.CharField(
        max_length=30, verbose_name="ФИО сотрудника", null=True
    )
    tel_number = models.IntegerField(
        blank=True, verbose_name="Телефон номер", default=0, null=True
    )
    service_specialty = models.CharField(
        max_length=30, verbose_name="услуги/специальности", null=True
    )
    length_of_service = models.CharField(
        max_length=6, verbose_name="стаж работы", null=True
    )
    calendar_register = models.ForeignKey(
        CalendarRegistration, on_delete=models.CASCADE, related_name="calendars"
    )

    class Meta:
        verbose_name = "Creating an Employee"

