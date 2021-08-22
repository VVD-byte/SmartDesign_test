from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from . import models, serializer


class CreateNewProductView(generics.CreateAPIView):
    """
    Создает записи о товарах
    Принимает json - {'name': 'xxx', 'description': 'xxx', 'options': [{'key':'', 'value': ''}, {'key':'', 'value': ''}]}
    Возвращает ошибку или данные о созданной записи
    """
    serializer_class = serializer.ProductSerializer


class GetNameProductView(generics.ListAPIView):
    """
    Возвращает названия и id товаров фильтруя их по названию и параметрам
    Принимает queryset - name=test&key=value&...
    """
    serializer_class = serializer.NameProductSerializer

    def get_queryset(self):
        queryset = models.Product.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        params = [{'key': i, 'value': self.request.query_params[i]} for i in self.request.query_params if i != 'name']
        params = params[0] if params.__len__() == 1 else params
        if params:
            return queryset.filter(**{'options': params})
        else:
            return queryset


class GetProductView(generics.ListAPIView):
    """
    Получить данные товара по id
    Принимает queryset - id=1
    Возвращает все данные о товаре с данным id
    """
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id']
