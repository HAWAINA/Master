from django.db import models


# Создание сотрудника логика находится тут:
class EmployeeCreation(models.Model):
    profile = models.ImageField(
        verbose_name="Профиль сотрудника", null=True
    )
    nickname = models.CharField(
        max_length=30, verbose_name="ФИО сотрудника", null=True
    )
    tel_number = models.IntegerField(
        blank=True, verbose_name="Телефон номер", null=True
    )
    service_specialty = models.CharField(
        max_length=30, verbose_name="услуги/специальности", null=True
    )
    length_of_service = models.CharField(
        max_length=6, verbose_name="стаж работы", null=True
    )

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
    profile_ref = models.ImageField(
        verbose_name="Смена Профиля сотрудника", null=True
    )
    nickname_ref = models.CharField(
        max_length=30, verbose_name="Смена ФИО сотрудника", null=True
    )
    tel_number_ref = models.IntegerField(
        verbose_name="Смена Телефон номер", null=True
    )
    service_specialty_ref = models.CharField(
        max_length=30, verbose_name="Смена услуги/специальности", null=True
    )
    length_of_service_ref = models.CharField(
        max_length=6, verbose_name="стаж работы", null=True
    )
    description_ref = models.TextField(
        max_length=2000, verbose_name="описание", null=True
    )

    class Meta:
        verbose_name = "Редактирование сотрудника"


class CalendarRefactor(models.Model):
    work_calendar_ref = models.DateField(verbose_name="Календарь", null=True)
    getting_started_ref = models.TimeField(verbose_name="Начало Работы")
    end_of_job_ref = models.TimeField(verbose_name="Конец Работы")
    lunch_start_ref = models.TimeField(verbose_name="Начала обеда", null=True)
    lunch_end_ref = models.TimeField(verbose_name="Конец обеда", null=True)

    class Meta:
        verbose_name = "Редактирование рабочий Календарь"
