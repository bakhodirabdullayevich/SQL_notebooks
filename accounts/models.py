from django.db import models
from django.contrib.auth.models import User

from objects.models import Organization


# Create your models here.
class Profile(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, )
    #photo = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} profili"