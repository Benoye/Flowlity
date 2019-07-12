import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.utils import json

from inventory.models import Product
from inventory.serializers import ProductSerializer, ProductModelSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        if self.queryset:
            return self.queryset

        with open("data/product.json") as json_file:
            p_list = json.load(json_file)

        p_obj = []
        for p in p_list:
            o = Product(
                pk=p['product_id'],
                name=p['product_name'],
                date=datetime.datetime.strptime(p['date'], "%d-%m-%Y"),
                inventory=p['inventory_level'],
            )
            p_obj.append(o)
        return p_obj

    # @action(detail=False)
    # def draw_graph_all(self, request):
    #     objects = self.get_queryset()
    #
    #     graph_data = [
    #         {'x': [], 'y': [], 'type': 'bar', 'name': 'SF'},
    #         {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    #     ]
    #     for o in objects:
    #         if
    #         graph_data.append({
    #             'x':
    #         })
