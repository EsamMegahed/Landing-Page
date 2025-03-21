from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils.translation import gettext as _
# Create your models here.


class Hajj(models.Model):
    title = models.CharField(_('Title'),max_length=255)
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Hajj Image'),upload_to='Hajj Images/',
                                  validators=[FileExtensionValidator(
                                      ['png', 'jpg', 'webp', 'apng', 'avif', 'jpeg']
                                      )])
    start_date = models.DateField(_('Start Date'))
    end_date = models.DateField(_('End Date'))
    location = models.CharField(_('Location'),max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.title} => Date From ({self.start_date}) To ({self.end_date})")

class Umrah(models.Model):
    title = models.CharField(_('Title'),max_length=255)
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Umrah Image'),upload_to='Umrah Images/',
                                  validators=[FileExtensionValidator(
                                      ['png', 'jpg', 'webp', 'apng', 'avif', 'jpeg']
                                      )])
    start_date = models.DateField(_('Start Date'))
    end_date = models.DateField(_('End Date'))
    location = models.CharField(_('Location'),max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(f"{self.title} => Date From ({self.start_date}) To ({self.end_date})")
