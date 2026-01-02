
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from apps.car.filter import CarFilter
from apps.car.models import CarModel
from apps.car.serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter

class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    http_method_names = ['get', 'put', 'patch', 'delete']