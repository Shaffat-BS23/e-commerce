from django.db import models
from django.utils.translation import gettext_lazy as _
import enum
from django.contrib.auth.models import AbstractUser as BaseUser
# Create your models here.


class UserTypes(models.IntegerChoices):
    Admin = 1, _('Admin')
    Vendor = 2, _('Vendor')
    Customer = 3, _('Customer')


class User(BaseUser):
    username = models.CharField(
        verbose_name=_('Username'),
        max_length=120,
        blank=False,
        null=False,
        help_text=_("Enter Username")
    )
    email = models.EmailField(
        verbose_name=_('Email Address'),
        blank=False,
        null=False,
        help_text=_('Enter Valid Email'),
        unique=True
    )
    phone = models.CharField(
        verbose_name='Phone Number',
        blank=True,
        null=True,
        max_length=20
    )
    user_type = models.IntegerField(
        verbose_name='User Type',
        blank=False,
        null=False,
        choices=UserTypes.choices,
        default=UserTypes.Customer
    )
