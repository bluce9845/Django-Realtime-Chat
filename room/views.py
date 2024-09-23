from django.contrib.auth.decorators import  login_required
from django.shortcuts import render
from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)

    return render(request, 'room/room.html', {'room': room})

def chat_room(request, room_name):
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages,
    })