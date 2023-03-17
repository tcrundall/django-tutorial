from django.shortcuts import render
from .models import Board

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(id=pk)
    topics = board.topics.all()
    topics = [f'topic {i}' for i in range(5)]
    return render(
        request,
        'board_topics.html',
        {'topics': topics, 'pk': pk}
    )

def user(request, username):
    return render(request, 'user.html', {'username': username})

