import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.utils import json

from inventory.models import Product
from inventory.serializers import ProductModelSerializer


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

    def retrieve(self, request, pk=None, *args, **kwargs):
        product_data = []
        for d in self.get_queryset():
            if d.id != int(pk):
                continue
            product_data.append(d)
        serializer = ProductModelSerializer(product_data, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def draw_graph(self, request, pk=None):
        graph_data_helper = {}
        objects = self.get_queryset()
        for o in objects:
            if pk != 'all' and int(pk) != o.id:
                continue
            if o.id in graph_data_helper.keys():
                graph_data_helper[o.id]['x'].append(o.date)
                graph_data_helper[o.id]['y'].append(o.inventory)
            else:
                graph_data_helper[o.id] = {'x': [o.date], 'y': [o.inventory], 'type': 'bar', 'name': o.name, 'id': o.id}
        return Response(graph_data_helper.values())
