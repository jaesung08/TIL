from rest_framework import serializers
from .models import DepositOptions, DepositProducts



class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    # read_only_fields 와 같은 역함
    # product = serializers.ReadOnlyField(source='DepsitOptions.product')
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)