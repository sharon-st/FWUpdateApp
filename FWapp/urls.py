from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FirmwarePackageViewSet, login_successful

from django.conf.urls.static import static
from django.conf import settings
# Define a router and register the viewset
router = DefaultRouter()
router.register(r'firmware-packages', FirmwarePackageViewSet, basename='firmwarepackage')


# App-level urlpatterns
urlpatterns = [
    path('Fws/', include(router.urls)),  # This will include all routes for FirmwarePackageViewSet
#   path('', FirmwarePackageViewSet, name='view_all_packages')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

