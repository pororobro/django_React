from rest_framework import serializers
from .models import BoardV0
from icecream import ic

class BoardSerializer(serializers.Serializer):
    # pk인 id는 99퍼센트 수정 안 할 것이므로 read_only
    title = serializers.CharField()
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return BoardV0.objects.create(**validated_data)