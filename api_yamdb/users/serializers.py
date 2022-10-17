"""Module with serializer of users app."""

from rest_framework import exceptions, serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class TokenSerializer(serializers.Serializer):
    """Serializer of token."""

    username = serializers.CharField(max_length=200, required=True)
    verification_code = serializers.CharField(max_length=200, required=True)

    def validate_username(self, value):
        """Validate username for token."""
        if not User.objects.filter(username=value).exists():
            raise exceptions.NotFound(f'There is no user {value}')
        return value


class AdminSerializer(serializers.ModelSerializer):
    """Serializer of user with admin role param."""

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        """Meta class for user admin serializer."""

        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')

    def validate_username(self, value):
        """Validate correct username."""
        if value == 'me':
            raise serializers.ValidationError('"me" is invalid username')
        return value


class StandartUserSerializer(serializers.ModelSerializer):
    """Serializer of user."""

    email = serializers.EmailField()

    class Meta:
        """Meta class of user serializer."""

        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')
        read_only_fields = ('role',)

    def validate_username(self, value):
        """Validate correct username."""
        if value == 'me':
            raise serializers.ValidationError('"me" is invalid username')
        return value
