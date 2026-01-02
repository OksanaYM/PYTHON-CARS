from django.db import models


class CarConditionChoices(models.TextChoices):
    NEW = 'new'
    USED = 'used'
    ALL = 'all'