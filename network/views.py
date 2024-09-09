from rest_framework import viewsets, permissions, filters
from .models import NetworkNode
from .permissions import IsActiveStaffUser
from .serializers import NetworkNodeSerializer


class IsActiveUser(permissions.BasePermission):
    """
    Разрешает доступ только активным пользователям.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_active


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    permission_classes = [IsActiveStaffUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['country']  # Позволяет фильтрацию объектов по стране

    def get_queryset(self):
        # Фильтрация по стране через параметр запроса 'country'
        country = self.request.query_params.get('country')
        if country:
            return self.queryset.filter(country__iexact=country)
        return self.queryset
