from django.shortcuts import render

from .models import Message

# Create your views here.

def index(request):
    messages = Message.objects.all()
    return render(request, 'render/index.html', context={'messages': messages})
