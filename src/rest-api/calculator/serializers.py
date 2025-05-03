from rest_framework import serializers

class CalculationSerializer(serializers.Serializer):
    expression = serializers.CharField()