from rest_framework import serializers
from class_status.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'arduino_id', 'image', 'gas_quality', 'air_quality')