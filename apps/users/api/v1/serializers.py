from rest_framework import serializers

from users.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'write_only': True},
            'is_active': {'write_only': True}
        }