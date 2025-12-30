from django.db import models


class CarShopModel(models.Model):
    class Meta:
        db_table = 'car_shops'

    name = models.CharField(max_length=50)
