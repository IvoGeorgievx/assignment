from django.core.exceptions import ValidationError


# validators with proper error when invalid data is entered.
def validate_length(value):
    if len(str(value)) != 10:
        raise ValidationError("Phone must contain exactly 10 digits")


def validate_name_length(value):
    if len(value) < 5:
        raise ValidationError("Names must contain at least 5 characters ")
