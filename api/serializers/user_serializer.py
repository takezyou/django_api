from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'profile', 'password')

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'], email=validated_data['email'])
