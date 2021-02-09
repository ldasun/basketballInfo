from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.get_test_api_view),
    path('players/<int:player_id>', views.get_player_api_view),
    path('players/getByTeam/', views.get_players_by_team_api_view),
    path('teams/<int:team_id>/getPlayersByPercentile/', views.get_players_by_percentile_api_view),
]