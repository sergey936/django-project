from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Games

def index(request):
    game_inf = Games.objects.all()
    return render(request, 'main/index.html', {'game_inf': game_inf})

def about(request):
    return render(request, 'main/about.html')


def show_game(request, game_id):
    game = get_object_or_404(Games, pk=game_id)


    return render(request, 'main/game.html', {'game': game})