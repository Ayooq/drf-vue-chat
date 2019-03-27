from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    """Модель комнаты чата."""

    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Создатель')
    participants = models.ManyToManyField(
        User, related_name='rooms', verbose_name='Участники')
    creation_date = models.DateTimeField(
        'Дата создания', auto_now_add=True)

    def get_participants(self):
        """Возвращает строку с именами участников беседы, разделёнными запятыми."""
        return ', '.join((person.username for person in self.participants.all()))

    get_participants.short_description = 'Участники'

    def __str__(self):
        return f'№{self.pk}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Message(models.Model):
    """Модель сообщения чата."""

    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, verbose_name='Комната чата')
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Отправитель')
    text = models.TextField(
        'Текст сообщения', max_length=500, editable=True)
    dispatch_date = models.DateTimeField(
        'Дата отправки', auto_now_add=True)

    def __str__(self):
        return f'№{self.pk}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
