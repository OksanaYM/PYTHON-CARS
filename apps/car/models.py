from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.car.choices.car_condition_choices import CarConditionChoices
from apps.car.choices.car_engine_choices import CarEngineChoices
from apps.car_shop.models import CarShopModel


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ['-year']

    types_of_cars = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    car_model = models.CharField(max_length=30)
    year = models.IntegerField(validators=[V.MinValueValidator(1950), V.MaxValueValidator(2026)])
    price = models.IntegerField(validators=[V.MinValueValidator(0)])
    car_condition = models.CharField(max_length=4, choices=CarConditionChoices.choices)
    engine = models.CharField(max_length=8, choices=CarEngineChoices.choices)
    car_shop = models.ForeignKey(CarShopModel, on_delete=models.CASCADE, related_name='cars')

