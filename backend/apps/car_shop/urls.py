from django.urls import path

from apps.car_shop.views import CarShopAddCarView, CarShopListCreateView

urlpatterns = [
    path('', CarShopListCreateView.as_view()),
    path('/<int:pk>/cars', CarShopAddCarView.as_view())
]