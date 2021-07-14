# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'htmx/index.html', {})

def room(request, room_name):
    return render(request, 'htmx/room.html', {
        'room_url': "connect:ws:localhost:8000/ws/chat/" + room_name + "/"
    })
