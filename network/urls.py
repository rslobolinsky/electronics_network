from rest_framework.routers import DefaultRouter
from .views import NetworkNodeViewSet

router = DefaultRouter()
router.register(r'nodes', NetworkNodeViewSet, basename='networknode')

urlpatterns = router.urls
