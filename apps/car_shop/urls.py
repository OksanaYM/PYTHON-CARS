from django.urls import path

from apps.car_shop.views import CarShopListCreateView

urlpatterns = [
    path('', CarShopListCreateView.as_view())
]