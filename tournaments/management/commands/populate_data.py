from django.db.models.fields import related
from accounts.models import Role
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from tournaments.models import Coach, Game, Player, PlayerStatistic, Season, Team, Tournament
import datetime


class Command(BaseCommand):

    def create_roles(self):
        ADMIN = 'A'
        COACH = 'C'
        PLAYER = 'P'

        ROLE_TYPES = [
            (ADMIN, 'Admin'),
            (COACH, 'Coach'),
            (PLAYER, 'Player'),
        ]

        for role in range(len(ROLE_TYPES)):
            try:
                role = Role(type=ROLE_TYPES[role])
            except ObjectDoesNotExist:
                raise CommandError('Role Does not exists')
            role.save()
            self.stdout.write(self.style.SUCCESS(''))

    def create_user(self, fake, first_name, last_name):
        userid = first_name+'.'+last_name
        user = User(username=userid.lower(), password='Test@test', email=fake.safe_email(),
                    first_name=first_name, last_name=last_name)
        print('before user id:'+str(user.id)+' username: '+userid)
        user.save()
        print('after user  id: '+str(user.id))
        return user

    def create_teams(self, fake):

        player_names = ['Kareem Abdul-Jabbar', 'Carmelo Anthony', 'Paul Arizin', 'Charles Barkley', 'Rick Barry', 'Elgin Baylor', 'Larry Bird', 'Carol Blazejowski',
                        'Manute Bol', 'Bill Bradley', 'Larry Brown', 'Kobe Bryant', 'Wilt Chamberlain', 'Cynthia Cooper', 'Bob Cousy', 'David Albert DeBusschere',
                        'Anne Donovan', 'Tim Duncan', 'Kevin Durant', 'Margo Dydek', 'Teresa Edwards', 'Wayne Embry', 'Julius Erving', 'Walt Frazier', 'Kevin Garnett',
                        'George Gervin', 'John Havlicek', 'Connie Hawkins', 'Elvin Hayes', 'John Isaacs', 'Allen Iverson', 'Phil Jackson', 'LeBron James',
                        'Dennis Wayne Johnson', 'Magic Johnson', 'Michael Jordan', 'Jason Kidd', 'Joe Lapchick', 'Nancy Lieberman', 'Jeremy Lin',
                        'Earl Lloyd', 'Rebecca Lobo', 'Jerry Lucas', 'Hank Luisetti', 'Moses Malone', 'Pete Maravich', 'Dick McGuire', 'George Mikan', 'Cheryl Miller',
                        'Earl Monroe', 'Alonzo Mourning', 'Landry Shamet', 'Don Nelson', 'Dirk Nowitzki', 'Hakeem Olajuwon', 'Shaquille O’Neal', 'Chris Paul', 'Gary Payton',
                        'Bob Pettit', 'Andrew Phillip','Marc Gasol','Danny Green','Serge Ibaka','Kawhi Leonard','Kyle Lowry','Pascal Siakam','Fred VanVleet','Norman Powell',
                        'Stephen Curry','Draymond Green','Shaun Livingston','Kevon Looney','Alfonzo McKinnie','Klay Thompson','Al-Farouq Aminu','Zach Collins','Seth Curry',
                        'Maurice Harkless','Rodney Hood','Enes Kanter','Damian Lillard','CJ McCollum','Evan Turner','Andre Iguodala','Giannis Antetokounmpo','Eric Bledsoe',
                        'Pat Connaughton','George Hill','Ersan Ilyasova','Brook Lopez','Khris Middleton','Will Barton','Malik Beasley','Torrey Craig','Gary Harris',
                        'Nikola Jokic','Paul Millsap','Monte Morris','Jamal Murray','Mason Plumlee','Andrew Bogut','Nikola Mirotic','Jodie Meeks','Jonas Jerebko',
                        'Jimmy Butler','Tobias Harris','JJ Redick','Ben Simmons','Jordan Bell','Quinn Cook','Garrett Temple','Clint Capela','Eric Gordon','Gerald Green',
                        'James Harden','Lou Williams','PJ Tucker','Joel Embiid','James Ennis','Tim Frazier','Meyers Leonard','Sterling Brown','Jonah Bolden',
                        'Boban Marjanovic','Greg Monroe','Austin Rivers','Mike Scott','TJ McConnell','Aron Baynes','Jaylen Brown','Gordon Hayward','Al Horford',
                        'Kyrie Irving','Marcus Morris','Terry Rozier','Jayson Tatum','Malcolm Miller','Tony Snell','Iman Shumpert','DJ. Wilson','Eric Moreland',
                        'Patrick McCaw','LaMarcus Aldridge','Marco Belinelli','DeMar DeRozan','Bryn Forbes','Rudy Gay','Patty Mills','Jakob Poeltl','Derrick White',
                        'Danuel House','Daniel Theis','Jonathon Simmons','Nene Hilario','Kenneth Faried','Malcolm Brogdon','Patrick Beverley','Danilo Gallinari',
                        'Shai Gilgeous-Alexander','JaMychal Green']

        coach = self.create_coach(fake, 'Lloyd Pierce')
        team = self.create_team('Atlanta Hawks', coach)
        for name in player_names[:10]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'Brad Stevens')
        team = self.create_team('Boston Celtics', coach)
        for name in player_names[10:20]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'Steve Nash')
        team = self.create_team('Brooklyn Nets', coach)
        for name in player_names[20:30]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'James Borrego')
        team = self.create_team('Charlotte Hornets', coach)
        for name in player_names[30:40]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'Billy Donovan')
        team = self.create_team('Chicago Bulls', coach)
        for name in player_names[40:50]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'Rick Carlisle')
        team = self.create_team('Dallas Mavericks', coach)
        for name in player_names[50:60]:
            self.create_player(fake, team, name)

        ######
        coach = self.create_coach(fake, 'Michael Malone')
        team = self.create_team('Denver Nuggets', coach)
        for name in player_names[60:70]:
            self.create_player(fake, team, name)

        ######
        coach = self.create_coach(fake, 'Dwane Casey')
        team = self.create_team('Detroit Pistons', coach)
        for name in player_names[70:80]:
            self.create_player(fake, team, name)
        
        ######
        coach = self.create_coach(fake, 'Steve Kerr')
        team = self.create_team('Golden State Warriors', coach)
        for name in player_names[80:90]:
            self.create_player(fake, team, name)

        ######
        coach = self.create_coach(fake, 'Stephen Silas')
        team = self.create_team('Houston Rockets', coach)
        for name in player_names[90:100]:
            self.create_player(fake, team, name)

        ######
        coach = self.create_coach(fake, 'Nate Bjorkgren')
        team = self.create_team('Indiana Pacers', coach)
        for name in player_names[100:110]:
            self.create_player(fake, team, name)

        ######
        coach = self.create_coach(fake, 'Tyronn Lue')
        team = self.create_team('Los Angeles Clippers', coach)
        for name in player_names[110:120]:
            self.create_player(fake, team, name)

        ######
        coach = self.create_coach(fake, 'Frank Vogel')
        team = self.create_team('Los Angeles Lakers', coach)
        for name in player_names[120:130]:
            self.create_player(fake, team, name)

        ######
        coach = self.create_coach(fake, 'Taylor Jenkins')
        team = self.create_team('Memphis Grizzlies', coach)
        for name in player_names[130:140]:
            self.create_player(fake, team, name)

        ######
        coach = self.create_coach(fake, 'Erik Spoelstra')
        team = self.create_team('Miami Heat', coach)
        for name in player_names[140:150]:
            self.create_player(fake, team, name)

        ######
        coach = self.create_coach(fake, 'Mike Budenholzer')
        team = self.create_team('Milwaukee Bucks', coach)
        for name in player_names[150:160]:
            self.create_player(fake, team, name)

        self.stdout.write(self.style.SUCCESS(
            'created all the objectes related to player team '))


    def create_coach(self, fake, name):
        names = name.split(' ')
        user = self.create_user(fake, names[0], names[1])
        coach = Coach(user_id=user.id)
        print('before coach '+str(coach.id)+' name: ' + name)
        coach.save()
        print('after coach '+' id: '+str(coach.id))
        return coach

    def create_team(self, name, coach):
        team = Team(name=name, coach=coach)
        print('before team '+str(team.id)+' name: '+str(name))
        team.save()
        print('after team '+' id: '+str(team.id))
        return team

    def create_player(self, fake, team,  player_name):
        names = player_name.split(' ')
        user = self.create_user(fake, names[0], names[1])
        player_height = fake.random_int(min=150, max=240)
        player = Player(user_id=user.id, team_id=team.id, height=player_height)
        print('before player '+str(player.id)+' name: ' + player_name)
        player.save()
        print('after player '+' id: '+str(player.id))
        return player




 
    def create_tournament(self):
        tournament = Tournament (name = 'NBA',country = 'USA')
        tournament.save()
        return tournament

    def create_season(self):
        tournament = self.create_tournament()
        season = Season(tournament_id= tournament.id, name='2020-21')
        season.save()
        return season

    def create_round(self,fake, no_of_games, teams, start_date, end_date, round_number):
        
        winning_teams=[]
        for i in range(0,no_of_games,2): 
            winning_teams.append(self.create_series(fake,teams[i],teams[i+1],start_date, end_date, round_number))
        
        return winning_teams

    def create_series(self,fake,team1, team2, start_date, end_date,round_number):
        
        team1_win_count=0
        team2_win_count=0

        for i in range(1,7):
            if(team1_win_count < 4 and team2_win_count < 4  ):
                if(i in [1,2,5,7]):
                   game = self.create_game(fake, team1,team2,fake.date_time_between(start_date, end_date),round_number)                   
                else :
                    game = self.create_game(fake, team2,team1,fake.date_time_between(start_date, end_date),round_number)
                if game.winning_team== team1 :
                    team1_win_count += 1
                else: 
                    team2_win_count += 1
        return team1 if team1_win_count > team2_win_count else team2


    def create_game(self, fake,home_team, away_team, game_date,round):
        home_team_score=fake.random_int(min=0, max=200)
        away_team_score=fake.random_int(min=0, max=200)
        winning_team = home_team if home_team_score > away_team_score else away_team 
        game = Game(season_id=1, home_team=home_team,away_team=away_team,home_team_score=home_team_score,away_team_score=away_team_score,winning_team=winning_team,date=game_date,round_number=round)
        game.save()
        return game


    def create_first_round(self, fake, teams):
        start_date =  datetime.date(year=2019, month=4, day=1) 
        end_date= datetime.date(year=2019, month=6, day=30) 
        round_number='FR'
        return self.create_round(fake, 15, teams, start_date, end_date, round_number)

    def create_quater_finals(self, fake, teams):
        start_date =  datetime.date(year=2019, month=6, day=1) 
        end_date= datetime.date(year=2019, month=7, day=30) 
        round_number='QF'
        return self.create_round(fake, 7, teams, start_date, end_date, round_number)


    def create_semi_finals(self, fake, teams):
        start_date =  datetime.date(year=2019, month=8, day=1) 
        end_date= datetime.date(year=2019, month=8, day=30) 
        round_number='SF'
        return self.create_round(fake, 3, teams, start_date, end_date, round_number)

    def create_fixtures(self,fake):
        self.stdout.write(self.style.SUCCESS(
            '***** fixure creation started *****'))
        self.create_season()
        teams = Team.objects.all()
        print("all teams we got :"+ str(len(teams)))
        qf_temas = self.create_first_round(fake,teams)
        print("QF teams we got :"+ str(len(qf_temas)))
        sf_temas = self.create_quater_finals(fake,qf_temas)        
        print("SF teams we got :"+ str(len(sf_temas)))
        final_teams = self.create_semi_finals(fake, sf_temas) 
        print("final teams we got :"+ str(len(final_teams)))
        self.create_game(fake,final_teams[0], final_teams[1],datetime.date(year=2019, month=9, day=1),'FI')
        self.stdout.write(self.style.SUCCESS(
            '***** fixure creation completed *****'))

    def calculate_player_score (self, fake, available_team_score):
        #assume max score can player can get 80
        max_personal_score = 80
        generated_score = fake.random_int(min=0, max=available_team_score)
        if (generated_score > max_personal_score):
            return fake.random_int(min=0, max=max_personal_score)
        else : 
            return generated_score

    def create_stats_for_team(self, fake, game, team, team_score):
                
        available_team_score= team_score
        players = Player.objects.filter(team_id=team.id)
        for i in range (len(players)-1):
            score = self.calculate_player_score(fake,available_team_score)
            player_statistic = PlayerStatistic( player = players[i], game = game , score = score)
            player_statistic.save()
            available_team_score -= score
        #create last team member start
        last_player_score = available_team_score if  available_team_score > 0 else 0 
        player_statistic = PlayerStatistic( player = players[len(players)-1] , game = game , score = last_player_score)
        player_statistic.save()


    def create_player_Statistics(self, fake):
        self.stdout.write(self.style.SUCCESS(
            '***** player statistic creation started *****'))
        games = Game.objects.all()
        for i in range (len(games)):
            self.create_stats_for_team(fake, games[i], games[i].away_team , games[i].away_team_score)
            self.create_stats_for_team(fake, games[i], games[i].home_team , games[i].home_team_score)

        self.stdout.write(self.style.SUCCESS(
            '***** player statistic creation completed *****'))
        
    

    def handle(self, *args, **options):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS(
            '***** Data population Started   *****'))
        # self.create_roles()
        # self.create_teams(fake)
        # self.create_fixtures(fake)
        self.create_player_Statistics(fake)

        self.stdout.write(self.style.SUCCESS(
            '***** Data population completed *****'))
