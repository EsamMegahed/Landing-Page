from django.db import models
from django.core.validators import FileExtensionValidator,MinValueValidator,MaxValueValidator
from django.utils.translation import gettext as _

# Create your models here.


class Hotel(models.Model):
    title = models.CharField(_('Title'),max_length=255)
    description = models.TextField(_('Description'))
    image = models.ImageField(_('Umrah Image'),upload_to='Hotel Images/',
                                  validators=[FileExtensionValidator(
                                      ['png', 'jpg', 'webp', 'apng', 'avif', 'jpeg']
                                      )])
    location = models.CharField(_('Location'),max_length=255)
    price = models.IntegerField(_('Price'),default=0)
    stars = models.IntegerField(_('Stars'),validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(f'{self.title} => Location : {self.location} | Price : {self.price} | stars : {self.stars}')
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = None
        return url