from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from business import views
from .yasg import urlpatterns as swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),

    # Создание сотрудника Api
    path("api/v1/employee_creation", views.EmployeeCreation),
    path("api/v1/calendar_register", views.CalendarRegistrationView),

    # Редактирование сотрудника Api
    path("api/v1/employee_refactor", views.EmployeeRefactorView),
    path("api/v1/calendar_refactor", views.CalendarRefactorView),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
