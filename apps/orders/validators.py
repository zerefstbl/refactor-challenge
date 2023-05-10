from django.core.validators import RegexValidator

def phone_validator():
    return RegexValidator(regex=r'^\d{1,15}$', message="Invalid phone number")