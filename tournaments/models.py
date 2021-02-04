from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.functional import cached_property
from django.db.models import Avg
import math


class Coach(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    def __str__(self):
        return 'Name : %s %s' % (self.user.first_name, self.user.last_name)

    def get_absolute_url(self):
        return reverse('coach', args=[str(self.id)])


class Team(models.Model):

    name = models.CharField(verbose_name='Name',
                            max_length=100, blank=False,  null=False)
    coach = models.OneToOneField(
        Coach, verbose_name='Coach', blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        ordering = ['name']

    def list_players_by_team(self):
        return Player.objects.filter(team=self)

    def list_players_by_percentile(self, percentile):
        #since team has 10 players maximum
        #count = 10-int(math.ceil((10 * percentile) / 100))
        player_list = PlayerStatistic.objects.filter().annotate(
            averaged_points=Avg('score')).order_by('averaged_points')
        count = int(math.ceil((len(player_list) * int(percentile)) / 100))
        selected_player_list = []
        for idx, val in enumerate(player_list):
            idx += 1
            if idx > count:
                player = Player.objects.get(id=val['player_id'])
                selected_player_list.append(player)
        return selected_player_list

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('team', args=[str(self.id)])


class Player(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    height = models.PositiveIntegerField(
        verbose_name='Height(cm)', default='0')

    @cached_property
    def full_name(self):
        return '{first_name} {last_name}'.format(first_name=self.user.first_name,
                                                 last_name=self.user.last_name)

    @cached_property
    def number_of_games(self):
        return PlayerStatistic.objects.filter(player=self).filter().count()

    @cached_property
    def average_score(self):
        return PlayerStatistic.objects.filter(player=self).aggregate(Avg('score'))

    def __str__(self):
        return 'Name : %s , Height : %s' % (self.user.first_name, self.height)

    def get_absolute_url(self):
        return reverse('player', args=[str(self.id)])


class Tournament(models.Model):
    name = models.CharField(verbose_name='Name',
                            max_length=100, blank=False,  null=False)
    country = models.CharField(verbose_name='Country',
                               max_length=100, blank=False,  null=False)


class Season(models.Model):
    name = models.CharField(verbose_name='Name',
                            max_length=100, blank=False,  null=False)
    tournament = models.ForeignKey(Tournament, on_delete=models.PROTECT)


class Game(models.Model):

    FR = 'FR'
    QF = 'QF'
    SF = 'SF'
    FI = 'FI'
    WI = 'WI'

    ROUNDS = [
        (FR, 'First Round'),
        (QF, 'Quarter Final'),
        (SF, 'Semi Final'),
        (FI, 'Final'),
        (WI, 'Winner')
    ]

    season = models.ForeignKey(
        Season, on_delete=models.PROTECT, related_name='season')
    home_team = models.ForeignKey(
        Team, on_delete=models.PROTECT, related_name='home_team')
    away_team = models.ForeignKey(
        Team, on_delete=models.PROTECT, related_name='away_team')
    home_team_score = models.PositiveIntegerField(default=0)
    away_team_score = models.PositiveIntegerField(default=0)
    winning_team = models.ForeignKey(
        Team, on_delete=models.PROTECT, related_name='winning_team')
    date = models.DateField(verbose_name='Game date')
    round_number = models.CharField(
        max_length=2,
        choices=ROUNDS,
        default=QF,
        verbose_name='Round type'
    )

    def __str__(self):
        return 'Game # %s , %s &  %s' % (str(self.id), self.away_team, self.home_team)

    def get_absolute_url(self):
        return reverse('game', args=[str(self.id)])


class PlayerStatistic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('player', 'game',)

    def __str__(self):
        return str(self.score)

    def get_absolute_url(self):
        return reverse('player_stat_detail', args=[str(self.id)])


class TeamStatistic(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='team')
    game = models.ForeignKey(
        Game, on_delete=models.CASCADE, related_name='game')
    score = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('team', 'game',)

    def __str__(self):
        'Game # %s , %s : %s' % (self.game.id, self.team.name, self.score)

    def get_absolute_url(self):
        return reverse('team_stat_detail', args=[str(self.id)])
