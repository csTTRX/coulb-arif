from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    #photo = models.ImageField(verbose_name="photo de profile", null= True, blank = True)
    user_date = models.DateField(null=True, blank= True)

    # IMAGE_MAX_SIZE = (300, 300)
    # def resize_image(self):
    #     photo = Image.open(self.photo)
    #     photo.thumbnail(self.IMAGE_MAX_SIZE)
    #     photo.save(self.photo.path)
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.resize_image()

    def __str__(self):

        if self.username:
            return self.username
        
        elif self.first_name and self.last_name:
            return self.first_name + "  " + self.last_name
        else:
            return self.email
