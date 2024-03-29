from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


def index(request):
    return render(request, 'whatsapp/index.html', {})

def room(request, room_name):
    return render(request, 'whatsapp/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })


