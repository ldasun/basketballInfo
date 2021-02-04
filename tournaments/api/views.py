from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view

from tournaments.api.serializers import PlayerSerializer
from tournaments.models import Player, Team


@api_view(["GET"])
def get_test_api_view(request):
    return JsonResponse({'tournament test': 'success'}, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_player_api_view(request, player_id=None):
    # return JsonResponse({'player':id}, status=status.HTTP_200_OK)
    player = get_object_or_404(Player, id=player_id)
    serializer = PlayerSerializer(player)
    return JsonResponse({'player': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_players_by_team_api_view(request):
    team_id = request.GET.get('team_id',None)
    #return JsonResponse({'team' : team_id}, status=status.HTTP_200_OK)
    team = get_object_or_404(Team, id=team_id)
    player_list = team.list_players_by_team()
    serializer = PlayerSerializer(player_list, many=True)
    return JsonResponse({'players': serializer.data}, safe=False, status=status.HTTP_200_OK)

    
@api_view(["GET"])
def get_players_by_percentile_api_view(request, team_id=None):
    percentile = request.GET.get('percentile', None)
    #return JsonResponse({'percentile': percentile, 'team_id': team_id}, status=status.HTTP_200_OK)
    team = get_object_or_404(Team, id=team_id)
    selected_players = team.list_players_by_percentile(percentile)
    serializer = PlayerSerializer(selected_players, many=True)
    return JsonResponse({'selected_players_in_' + str(percentile) + '_percentile': serializer.data}, safe=False,
                        status=status.HTTP_200_OK)


