from django.db import models
def firmware_upload_path(instance, filename):
    # Define the directory to save the uploaded firmware packages
    return f'firmware_packages/{instance.name}/{filename}'

class FirmwarePackage(models.Model):
    name= models.CharField(max_length=200)
    version=models.CharField(max_length=10)
    updated_by=models.CharField(max_length=20)
    note=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #fw_package_url= models.URLField()
    fw_package = models.FileField(upload_to=firmware_upload_path)

    def __str__(self):
        return f"{self.name} - {self.version}"