from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from business import views
from .yasg import urlpatterns as swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    # Создание сотрудника Api
    path("api/v1/employee_creation", views.employee_view),
    path("api/v1/calendar_register", views.calendar_view),
    # Редактирование сотрудника Api
    path("api/v1/employee_refactor/<int:id>", views.employee_refactor_view),
    path("api/v1/calendar_refactor", views.calendar_refactor_view),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
