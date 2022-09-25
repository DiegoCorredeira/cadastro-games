import django.forms
from .models import Games


class GamesForm(django.forms.ModelForm):
    ativo = django.forms.CharField(
        widget=django.forms.TextInput(
            attrs={"type": "text"}
        )
    )

    class Meta:
        model = Games
        fields = ['nome', 'qtd_trofeus', 'ativo']
