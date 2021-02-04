from django.contrib import admin

from .models import (Coach, Game, Player, PlayerStatistic, Season, Team,
                     TeamStatistic, Tournament)

models = [Coach, Game, Player, Season, Team,
          Tournament, PlayerStatistic, TeamStatistic]
admin.site.register(models)
