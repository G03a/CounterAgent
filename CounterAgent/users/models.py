import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    COMPANY = 'COMP'
    PRIVATE_PERSON ='PRIV'
    COMPANY_PRIVATE = [
        (COMPANY, "Компанія"),
        (PRIVATE_PERSON, "Приватна особа")
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(verbose_name="Повне іменування", max_length=250,
                                 unique=True, null=True, blank=True)
    status = models.CharField(verbose_name="Юр/Фізична особа", max_length=50, choices=COMPANY_PRIVATE,
                              default=COMPANY)
