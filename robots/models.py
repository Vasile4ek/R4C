from django.db import models
from django.core.validators import MinLengthValidator

class Robot(models.Model):
    serial = models.CharField(max_length=5, blank=False, null=False, validators=[MinLengthValidator(5)])
    model = models.CharField(max_length=2, blank=False, null=False, validators=[MinLengthValidator(2)])
    version = models.CharField(max_length=2, blank=False, null=False, validators=[MinLengthValidator(2)])
    created = models.DateTimeField(blank=False, null=False)
