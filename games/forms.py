import django.forms
from .models import Games


class GamesForm(django.forms.ModelForm):
    class Meta:
        model = Games
        fields = ['nome', 'qtd_trofeus', 'ativo']
