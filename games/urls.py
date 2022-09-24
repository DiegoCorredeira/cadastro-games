from django.urls import path
from .views import ListaGamesView, GamesCreateView

urlpatterns = [
    path('', ListaGamesView.as_view(), name='games.index'),
    path('novo/', GamesCreateView.as_view(), name="games.novo")
]
