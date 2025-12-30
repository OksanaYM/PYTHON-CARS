from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from apps.car.serializers import CarSerializer
from apps.car_shop.models import CarShopModel
from apps.car_shop.serializers import CarShopSerializer


class CarShopListCreateView(ListCreateAPIView):
    serializer_class = CarShopSerializer
    queryset = CarShopModel.objects.all()

class CarShopAddCarView(GenericAPIView):
    queryset = CarShopModel.objects.all()

    def post(self, *args, **kwargs):
        car_shop = self.get_object()
        data = self.request.data
        serializer = CarSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(car_shop_id=car_shop.id)
        car_serializer = CarShopSerializer(car_shop)
        return Response(car_serializer.data, status=status.HTTP_201_CREATED)
