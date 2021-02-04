from accounts.models import Role
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from tournaments.models import Coach, Player, Team


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
        user = User(username=userid, password='Test@test', email=fake.safe_email(),
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
                        'Earl Monroe', 'Alonzo Mourning', 'Steve Nash', 'Don Nelson', 'Dirk Nowitzki', 'Hakeem Olajuwon', 'Shaquille O’Neal', 'Chris Paul', 'Gary Payton',
                        'Bob Pettit', 'Andrew Phillip']

        coach = self.create_coach(fake, 'Roy Williams')
        team = self.create_team('Atlanta Hawks', coach)
        for name in player_names[:10]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'Red Auerbach')
        team = self.create_team('Boston Celtics', coach)
        for name in player_names[10:20]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'Gregg Popovich')
        team = self.create_team('Chicago Bulls', coach)
        for name in player_names[20:30]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'Pat Riley')
        team = self.create_team('Dallas Mavericks', coach)
        for name in player_names[30:40]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'Bill Self')
        team = self.create_team('Denver Nuggets', coach)
        for name in player_names[40:50]:
            self.create_player(fake, team, name)

        coach = self.create_coach(fake, 'Lenny Wilkens')
        team = self.create_team('Houston Rockets', coach)
        for name in player_names[50:60]:
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

    def handle(self, *args, **options):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS(
            '***** Data population Started   *****'))
        self.create_roles()
        self.create_teams(fake)

        self.stdout.write(self.style.SUCCESS(
            '***** Data population completed *****'))
