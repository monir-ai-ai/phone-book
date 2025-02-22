from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def validate_name(value):
    if not value.isalpha():
        raise ValidationError(
            gettext_lazy('Name should only contain alphabetical characters (A-Z).'),
            params={'value': value},
        )

def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError(
            gettext_lazy('Phone number should only contain digits (0-9).'),
            params={'value': value},
        )


class Contact(models.Model):
    first_name = models.CharField(max_length=50, validators=[validate_name])
    last_name = models.CharField(max_length=50, validators=[validate_name])
    phone_number = models.CharField(max_length=11, validators=[validate_phone_number])
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



