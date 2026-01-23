from django.db import models


class CarEngineChoices(models.TextChoices):
    PETROL = 'petrol'
    DIESEL = 'diesel'
    ELECTRIC = 'electric'
    HYBRID = 'hybrid'
    GAS = 'gas'