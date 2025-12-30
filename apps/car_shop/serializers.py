from rest_framework import serializers

from apps.car_shop.models import CarShopModel


class CarShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarShopModel
        fields = ('id', 'name')