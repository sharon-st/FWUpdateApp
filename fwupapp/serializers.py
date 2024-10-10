from rest_framework import serializers
from models import FirmwarePackage

class FirmwarePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model=FirmwarePackage
        fields = ['name', 'version','updated_by','note','upload_time','fw_package_url']