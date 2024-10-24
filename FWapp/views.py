from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import FirmwarePackage
from .serializers import FirmwarePackageSerializer
from django.http import HttpResponse
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from rest_framework import filters
# View for login success
def login_successful(request):
    return HttpResponse('Login Success')

class FirmwarePackageViewSet(viewsets.ModelViewSet):
    queryset = FirmwarePackage.objects.all()
    serializer_class = FirmwarePackageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'version']
    
     #action to download firmware by package ID
    @action(detail=True, methods=['get'], url_path='download')
    def download_firmware(self, request, pk=None):
        firmware = get_object_or_404(FirmwarePackage, pk=pk)
        if firmware.FW_package:
            file_path = firmware.FW_package.path  # Absolute path to the file
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
        return Response({"error": "File not found"}, status=404)
    
    