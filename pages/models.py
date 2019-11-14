from django.db import models
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your models here.
image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/pages/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}pages/'.format(settings.MEDIA_URL),
)
def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/my_sell/picture/<filename>
    return u'photos/{0}'.format( filename)
