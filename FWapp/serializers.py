from rest_framework import serializers
from .models import FirmwarePackage

class FirmwarePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=FirmwarePackage
        fields = ['name', 'version','updated_by','note','created_at','fw_package']
