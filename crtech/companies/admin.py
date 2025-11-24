from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "status", "last_update", "application_link")
