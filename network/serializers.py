from rest_framework import serializers
from .models import NetworkNode


class NetworkNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetworkNode
        fields = [
            'id', 'name', 'email', 'country', 'city', 'street', 'house_number',
            'level', 'supplier', 'debt', 'created_at'
        ]
        read_only_fields = ['debt']  # Запрет на изменение поля «Задолженность перед поставщиком»

    def update(self, instance, validated_data):
        # Удаление поля 'debt' из validated_data, если оно присутствует
        validated_data.pop('debt', None)
        return super().update(instance, validated_data)
