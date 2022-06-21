from django.db import models


# Создание сотрудника логика находится тут:
class EmployeeCreation(models.Model):
    profile = models.ImageField(verbose_name="Профиль сотрудника")
    nickname = models.CharField(max_length=30, verbose_name="ФИО сотрудника")
    tel_number = models.IntegerField(max_length=12, verbose_name="")
    service_specialty = models.CharField('+996', max_length=30)
    length_of_service = models.CharField(max_length=6)

    class Meta:
        verbose_name = "Создание сотрудника"


class CalendarRegistration(models.Model):
    work_calendar = models.DateField(verbose_name="Календарь")
    getting_started = models.TimeField(verbose_name="Начало Работы")
    end_of_job = models.TimeField(verbose_name="Конец Работы")
    lunch_start = models.TimeField(verbose_name="Начала обеда", null=True)
    lunch_end = models.TimeField(verbose_name="Конец обеда", null=True)

    class Meta:
        verbose_name = "Рабочий Календарь"


# Редактирование сотрудника логика находится тут:
class EmployeeRefactor(models.Model):
    profile = models.ImageField(verbose_name="Профиль сотрудника")
    nickname = models.CharField(max_length=30, verbose_name="ФИО сотрудника")
    tel_number = models.IntegerField(max_length=12, verbose_name="")
    service_specialty = models.CharField('+996', max_length=30)
    length_of_service = models.CharField(max_length=6)

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
