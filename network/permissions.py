from rest_framework.permissions import BasePermission


class IsActiveStaffUser(BasePermission):
    """
    Позволяет доступ только активным сотрудникам (is_active=True и is_staff=True).
    """

    def has_permission(self, request, view):
        # Проверяем, что пользователь аутентифицирован, активен и является сотрудником
        return request.user and request.user.is_active and request.user.is_staff
