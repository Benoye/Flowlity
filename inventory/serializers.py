from rest_framework import serializers

from inventory.models import Product


class ProductSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    date = serializers.DateTimeField()
    name = serializers.CharField(max_length=200)
    inventory = serializers.IntegerField()


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
