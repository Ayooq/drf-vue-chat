from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer


class RoomView(APIView):
    """Представление для комнат чата."""

    def get(self, request):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response({'rooms': serializer.data})


class MessageView(APIView):
    """Представление для сообщений чата."""

    def get(self, request):
        current_room = request.query_params.get('room')
        queryset = Message.objects.filter(room=current_room)
        serializer = MessageSerializer(queryset, many=True)
        return Response({'messages': serializer.data})

    def post(self, request):
        serializer = MessageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(sender=request.user)

            location = reverse('chat:dialogs', request=request)
            location_header = {'Location': location}

            return Response('Сообщение добавлено.', status=status.HTTP_201_CREATED, headers=location_header)

        return Response('Отправленные данные некорректны!', status=status.HTTP_406_NOT_ACCEPTABLE)
