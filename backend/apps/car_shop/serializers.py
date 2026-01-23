from rest_framework import serializers

from apps.car.serializers import CarSerializer
from apps.car_shop.models import CarShopModel


class CarShopSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    class Meta:
        model = CarShopModel
        fields = ('id', 'name', 'cars')