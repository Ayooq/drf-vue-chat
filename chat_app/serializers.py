from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Room, Message


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для моделей пользователей чата."""

    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializer(serializers.ModelSerializer):
    """Сериализатор для моделей комнат чата."""

    creator = UserSerializer()
    participants = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = '__all__'


class MessageGetSerializer(serializers.ModelSerializer):
    """Сериализатор для моделей сообщений чата."""

    sender = UserSerializer()

    class Meta:
        model = Message
        fields = '__all__'


class MessagePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('room', 'text')
