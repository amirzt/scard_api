from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


from users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    class AppType(models.TextChoices):
        bazar = 'bazar'
        myket = 'myket'
        googleplay = 'googleplay'
        web = 'web'
        ios = 'ios'

    phone = models.CharField(max_length=11, null=False, blank=False, unique=True)

    is_visible = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joint = models.DateField(auto_now_add=True)

    app_type = models.CharField(default=AppType.bazar, choices=AppType.choices, max_length=20)
    version = models.CharField(default='0.0.0', max_length=20)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone
