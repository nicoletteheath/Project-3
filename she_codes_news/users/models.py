from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    pass #this is where I would put my own fields (like profile pic)
    

    def __str__(self):
        return self.username
