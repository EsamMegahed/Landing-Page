from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Contact(models.Model):
    name = models.CharField(_('Name'),max_length=255)
    email = models.CharField(_('Email'),max_length=255)
    phone = models.CharField(_('Phone'),max_length=255)
    subject = models.CharField(_('Subject'),max_length=255)
    message = models.TextField(_('Message'))
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(f"{self.name} => Subject : ({self.subject})")
