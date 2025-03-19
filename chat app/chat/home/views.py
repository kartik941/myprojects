from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')
def Room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    Room = request.POST['room_name']
    username = request.POST['username']
    if room.objects.filter(name=Room).exist():
        return redirect('/'+Room+'/?username='+username)
    else:
        new_room = room.objects.create(name = Room)
        new_room.save()
        return redirect('/'+Room+'/?username='+username)