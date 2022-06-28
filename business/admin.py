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


admin.site.register(models.EmployeeCreation, EmployeeAdmin)
admin.site.register(models.CalendarRegistration, CalendarAdmin)
admin.site.register(models.EmployeeRefactor)
admin.site.register(models.CalendarRefactor)
