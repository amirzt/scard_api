from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.crypto import get_random_string

from users.managers import CustomUserManager


def get_yesterday_date():
    from datetime import date, timedelta
    return date.today() - timedelta(days=1)


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
    expire_date = models.DateTimeField(null=True, blank=True, default=get_yesterday_date)

    app_type = models.CharField(default=AppType.bazar, choices=AppType.choices, max_length=20)
    version = models.CharField(default='0.0.0', max_length=20)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone


class Shop(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    logo = models.ImageField(upload_to='shop/logo', null=True, blank=True)
    banner = models.ImageField(upload_to='shop/banner', null=True, blank=True)
    phone = models.CharField(max_length=11, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    score = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Offer(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    discount = models.FloatField(default=0.0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'offer']

    def __str__(self):
        return f'{self.user} - {self.offer}'


def get_otp():
    chars = '0123456789'
    code = get_random_string(length=4, allowed_chars=chars)
    return code


class OTP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, null=False, blank=False, default=get_otp)
    created_at = models.DateField(auto_now_add=True)


class HomeMessage(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(max_length=400, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateField(auto_now_add=True)


class Support(models.Model):
    phone = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telegram = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.phone
