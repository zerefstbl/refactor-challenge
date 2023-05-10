from django.db import models

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from datetime import datetime

from apps.categories.models import Categories

from apps.orders.validators import phone_validator

class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="orders",
    )
    
    order_category = models.ForeignKey(
        Categories,
        on_delete=models.PROTECT,
        to_field="name",
    )
    
    contact_name = models.CharField(
        max_length=100,
        help_text=_("Requester Name"),
        verbose_name=_("Contact Name"),
    )
    
    contact_phone = models.CharField(
        max_length=32,
        verbose_name=_("Contact Number"),
        help_text=_("Requester number"),
        validators=[phone_validator],
    )

    agency = models.CharField(
        max_length=150,
        verbose_name=_("Agency"),
        editable=False,
    )
    
    order_description = models.TextField()
    
    company = models.CharField(
        max_length=100,
        verbose_name=_("Company"),
        help_text=_("Provider service company")
    )

    deadline = models.DateTimeField(
        help_text=_("Limit date"),
        verbose_name=_("DeadLine")
    )
    
    @property
    def time_until_deadline(self):
        return self.deadline - datetime.now()

    def __str__(self):
        return f'{self.contact_name} - {self.agency}'
    
    class Meta:
        # Indexes is to optimize the code when filtering by the fields below
        indexes = [
            models.Index(fields=['contact_name', 'agency', 'company'])
        ]