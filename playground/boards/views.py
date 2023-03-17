from django.shortcuts import render
from .models import Board

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def user(request, username=''):
    return render(request, 'user.html', {'username': username})

