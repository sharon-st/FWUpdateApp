from rest_framework import viewsets
from models import FirmwarePackage
from serializers import FirmwarePackageSerializer

class FirmwarePackageViewSet():
    queryset= FirmwarePackage.objects.all()
    serializer_class = FirmwarePackageSerializer