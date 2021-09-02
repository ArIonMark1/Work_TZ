from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class BaseUser(AbstractUser):

    def __str__(self):
        return f'{self.username}'


class Profile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, null=False, unique=True)

    @receiver(post_save, sender=BaseUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=BaseUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
