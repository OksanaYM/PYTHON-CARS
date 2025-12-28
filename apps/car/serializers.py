from rest_framework import serializers

from apps.car.models import CarModel


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'types_of_cars', 'brand', 'car_model', 'price', 'year', 'created_at', 'updated_at')