from django.db import models
from django.utils.timezone import now

# Create your models here.
from django.db.models import URLField


class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(
        choices=CompanyStatus.choices, default=CompanyStatus.HIRING
    )
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = URLField(blank=True, max_length=100)

    def __str__(self):
        return self.name
