from django.urls import path, include

from .views import RoomView, MessageView


app_name = 'chat'
urlpatterns = [
    path('rooms/', RoomView.as_view(), name='rooms'),
    path('dialogs/', MessageView.as_view(), name='dialogs'),
]
