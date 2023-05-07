from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email adress"))
        
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        validate_email(email)
        
        user = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user
    
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, **extra_fields)
    
    def create_super_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)
        