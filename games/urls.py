from django.urls import path
from .views import ListaGamesView, GamesCreateView, GamesUpdateView, GamesDeleteView

urlpatterns = [
    path('', ListaGamesView.as_view(), name='games.index'),
    path('novo/', GamesCreateView.as_view(), name="games.novo"),
    path('editar/<int:pk>', GamesUpdateView.as_view(), name="games.editar"),
    path('remover/<int:pk>', GamesDeleteView.as_view(), name="games.remover")
]
