from django.db import models
from django.core.validators import FileExtensionValidator,MinValueValidator,MaxValueValidator
from django.utils.translation import gettext as _
# Create your models here.

class Comment(models.Model):
    name = models.CharField(_('Name'),max_length=255)
    comment = models.TextField(_('Comment'))
    date = models.DateField(_('Date'))
    country = models.CharField(_('country'),max_length=255)
    stars = models.IntegerField(_('Stars'),validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(f"{self.name} => Country: {self.country} / {self.stars}")
    