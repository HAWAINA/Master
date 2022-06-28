from django.contrib import admin
from . import models


class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nickname",
    )

    list_display_links = (
        "id",
        "nickname",
    )


class CalendarAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "work_calendar",
    )

    search_fields = ("nickname".split())

    list_display_links = (
        "id",
        "work_calendar"
    )


admin.site.register(models.Employee, EmployeeAdmin)
admin.site.register(models.Calendar, CalendarAdmin)
