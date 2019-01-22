from django.contrib import admin
from .models import File,FileUpload

admin.site.register(File)
admin.site.register(FileUpload)