from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Games
from .forms import GamesForm


class ListaGamesView(ListView):
    model = Games
    queryset = Games.objects.all().order_by('nome')


class GamesCreateView(CreateView):
    model = Games
    form_class = GamesForm
    success_url = '/games/'
