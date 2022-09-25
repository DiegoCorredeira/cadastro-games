from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Games
from .forms import GamesForm


class ListaGamesView(ListView):
    model = Games
    queryset = Games.objects.all().order_by('nome')

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro_nome = self.request.GET.get('nome') or None
        
        if filtro_nome:
            queryset = queryset.filter(nome__contains=filtro_nome)
        return queryset


class GamesCreateView(CreateView):
    model = Games
    form_class = GamesForm
    success_url = '/games/'


class GamesUpdateView(UpdateView):
    model = Games
    form_class = GamesForm
    success_url = '/games/'


class GamesDeleteView(DeleteView):
    model = Games
    success_url = '/games/'
