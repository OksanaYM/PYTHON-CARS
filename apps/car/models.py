from django.db import models

from core.models import BaseModel

from apps.car_shop.models import CarShopModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    types_of_cars = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    year = models.IntegerField()
    price = models.IntegerField()
    car_shop = models.ForeignKey(CarShopModel, on_delete=models.CASCADE, related_name='cars')
