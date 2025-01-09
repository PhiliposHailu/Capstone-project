from django.db import models
from django.contrib.auth.models import AbstractUser

#just incase I decide to customized in the future
class CustomUser(AbstractUser):
    email =                         models.EmailField(unique=True, blank=False, max_length=100)
    joined_at=                     models.DateTimeField(auto_now_add=True, blank=True)

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
