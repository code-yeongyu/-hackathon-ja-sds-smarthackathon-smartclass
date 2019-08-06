from rest_framework import serializers
from image_handle.models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'arduino_id', 'image', 'gas_quality', 'air_quality')