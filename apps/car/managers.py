from django.db import models


class CarQueryset(models.QuerySet):
    pass

class CarManager(models.Manager):
    def get_queryset(self):
        return CarQueryset(self.model)

