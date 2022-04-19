from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)