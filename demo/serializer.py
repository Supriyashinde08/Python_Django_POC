from demo.models import Productdetails
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productdetails
        fields = ['id', 'name', 'description', 'category', 'brand', 'size']
