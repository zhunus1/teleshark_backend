from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .managers import TeleSharkUserManager
# Create your models here.

class TeleSharkUser(AbstractUser):
    
    username = None

    email = models.EmailField(
        verbose_name = ("Email"),
        unique = True
    )

    first_name = models.CharField(
        verbose_name = ("First name"),
        max_length = 127,
    )

    last_name = models.CharField(
        verbose_name = ("Last name"),
        max_length = 127,
    )
    
    birthday = models.DateField(
        verbose_name = ("Birthday"),
        null = True,
        blank = True,
    )

    phone_number = PhoneNumberField(
        verbose_name = "Phone number",
        null = True,
        blank = True,
    )

    created = models.DateTimeField(
        verbose_name = ("Created"),
        auto_now_add = True,
    )

    updated = models.DateTimeField(
        verbose_name = ("Updated"),
        auto_now = True,
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ()

    objects = TeleSharkUserManager()

    class Meta:

        verbose_name = ("TeleSharkUser")
        verbose_name_plural = ("TeleSharkUsers")
        ordering = ('-created',)

    def __str__(self):
        return '%s' % self.email