from django.core import validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def PhoneValidator(value):
    if not value.isnumeric:
        raise ValidationError(
            _("Phone Number should contain only numbers")
        )

