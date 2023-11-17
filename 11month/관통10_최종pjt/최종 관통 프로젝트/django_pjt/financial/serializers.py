from rest_framework import serializers
from .models import *


# 예금
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
        
# 적금
class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    # read_only_fields 와 같은 역함
    # product = serializers.ReadOnlyField(source='DepsitOptions.product')
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)