from django.db import models


# Создание сотрудника логика находится тут:
class EmployeeCreation(models.Model):
    class Meta:
        verbose_name = "Создание сотрудника"


class EmployeeRegistration(models.Model):
    class Meta:
        verbose_name = "Регистрация сотрудника"


class Calendar(models.Model):
    work_calendar = models.DateField(verbose_name="Календарь")
    getting_started = models.TimeField(verbose_name="Начало Работы")
    end_of_job = models.TimeField(verbose_name="Конец Работы")
    lunch_start = models.TimeField(verbose_name="Начала обеда", null=True)
    lunch_end = models.TimeField(verbose_name="Конец обеда", null=True)

    class Meta:
        verbose_name = "Рабочий Календарь"


# Редактирование сотрудника логика находится тут:
class EmployeeRefactor(models.Model):
    class Meta:
        verbose_name = "Редактирование сотрудника"


class CalendarRefactor(models.Model):
    work_calendar_ref = models.DateField(verbose_name="Календарь")
    getting_started_ref = models.TimeField(verbose_name="Начало Работы")
    end_of_job_ref = models.TimeField(verbose_name="Конец Работы")
    lunch_start_ref = models.TimeField(verbose_name="Начала обеда", null=True)
    lunch_end_ref = models.TimeField(verbose_name="Конец обеда", null=True)

    class Meta:
        verbose_name = "Рабочий Календарь редактирование"
