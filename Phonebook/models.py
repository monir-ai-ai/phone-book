from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def validate_alphabetical_name(value):
    """
    Validate that the name contains only alphabetical characters.
    """
    if not value.isalpha():
        raise ValidationError(
            gettext_lazy('Name should only contain alphabetical characters (A-Z).'),
            params={'value': value},
        )

def validate_numeric_phone_number(value):
    """
    Validate that the phone number contains only digits.
    """
    if not value.isdigit():
        raise ValidationError(
            gettext_lazy('Phone number should only contain digits (0-9).'),
            params={'value': value},
        )


class Contact(models.Model):
    """
    Model representing a contact entry in the phonebook.
    """
    first_name = models.CharField(max_length=50, validators=[validate_alphabetical_name])
    last_name = models.CharField(max_length=50, validators=[validate_alphabetical_name])
    phone_number = models.CharField(max_length=11, validators=[validate_numeric_phone_number])
    address = models.TextField()
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"



