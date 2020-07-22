from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    photo = models.FileField(upload_to='images/photoprofile')
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("user")
        verbose_name_plural = ("users")

    def __str__(self):
        return self.user.username

