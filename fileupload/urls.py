from django.conf.urls import url
from . import views

app_name='fileupload'

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^(?P<file_id>[0-9]+)/$', views.detail, name='detail'),
    # url(r'^upload/$',views.FileUploadd.as_view(), name='file-upload'),
    url(r'^upload/$',views.upload, name='upload'),
    url(r'^uploading/(?P<fileid>[0-9]+)/$',views.uploading, name='uploading'),
    url(r'^upload/process/$',views.uploadprocess, name='upload-process')
]