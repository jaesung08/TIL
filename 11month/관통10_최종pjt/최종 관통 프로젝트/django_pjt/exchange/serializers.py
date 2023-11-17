# converter/serializers.py
from rest_framework import serializers

class CurrencyConversionListSerializer(serializers.Serializer):
    cur_unit = serializers.CharField()
    deal_bas_r = serializers.CharField()
    cur_nm = serializers.CharField()
