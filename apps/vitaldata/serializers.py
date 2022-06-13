from rest_framework import serializers
from .models import VitalData

class VitalDataSerializer(serializers.ModelSerializer):
    """重点数据序列化器"""
    class Meta:
        model = VitalData
        fields = '__all__'

