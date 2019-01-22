from django.db import models
from django.urls import reverse

class File(models.Model):
    filename = models.CharField(max_length=250)
    path = models.CharField(max_length=1000)
    def get_absolute_url(self):
        return  reverse('fileupload:detail', kwargs={'pk':self.pk})
    def __str__(self):
        return self.filename + '-' + self.path

class FileUpload(models.Model):
    image = models.FileField()
    def get_absolute_url(self):
        # return  reverse('fileupload:file-upload')
        # return reverse('fileupload:file-upload', kwargs={'pk': self.pk})
        return reverse('fileupload:uploading',args=(self.id,))
        # return reverse('fileupload:uploading', kwargs={'project_id': self.id})

