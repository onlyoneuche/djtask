# Serializers define the API representation.

from core.tasks import create_random_user_accounts
from rest_framework import serializers
from django.contrib.auth import get_user_model

class CreateRandomUserSerializer(serializers.Serializer):
    """Serializer for the users object"""

    total = serializers.IntegerField()

    def create(self, validated_data):
        """Create random users"""
        create_random_user_accounts.delay(validated_data['total'])
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'first_name', 'last_name')
        #extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}