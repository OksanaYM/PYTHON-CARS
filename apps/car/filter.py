# from django_filters import rest_framework as filters
#
# from apps.car.serializers import CarSerializer
#
#
# class CarFilter(filters.FilterSet):
#     types_of_cars_starts_with = filters.CharFilter(field_name='types_of_cars', lookup_expr='startswith')
#     types_of_cars_ends_with = filters.CharFilter(field_name='types_of_cars', lookup_expr='endswith')
#     types_of_cars_contains = filters.CharFilter(field_name='types_of_cars', lookup_expr='contains')
#     car_model_starts_with = filters.CharFilter(field_name='car_model', lookup_expr='startswith')
#     car_model_ends_with = filters.CharFilter(field_name='car_model', lookup_expr='endswith')
#     car_model_contains = filters.CharFilter(field_name='car_model', lookup_expr='contains')
#     brand_starts_with = filters.CharFilter(field_name='brand', lookup_expr='startswith')
#     brand_ends_with = filters.CharFilter(field_name='brand', lookup_expr='endswith')
#     brand_contains = filters.CharFilter(field_name='brand', lookup_expr='contains')
#     price_lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
#     price_gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
#     price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte')
#     price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte')
#     year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
#     year_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
#     year_lte = filters.NumberFilter(field_name='year', lookup_expr='lte')
#     year_gte = filters.NumberFilter(field_name='year', lookup_expr='gte')
#     order = filters.OrderingFilter(
#         fields=CarSerializer.Meta.fields,
#     )
