from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Role(models.Model):

    ADMIN = 'A'
    COACH = 'C'
    PLAYER = 'P'

    ROLE_TYPES = [
        (ADMIN, 'Admin'),
        (COACH, 'Coach'),
        (PLAYER, 'Player'),
    ]

    type = models.CharField(max_length=2, choices=ROLE_TYPES,
                            default=PLAYER, verbose_name='Role Type')

    class Meta:
        ordering = ['type']

    def __str__(self):
        return str(self.type)

    def get_id(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('role_detail', args=[str(self.id)])


class UserRole(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_logged_in = models.BooleanField(default=False)

    def __str__(self):
        return 'Name : %s , Type : %s' % (self.user.first_name, self.role.type)

    def get_absolute_url(self):
        return reverse('user_role', args=[str(self.id)])


class UserStatistic(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    login_time = models.DateTimeField(
        verbose_name='login date time', default=timezone.now)
    logout_time = models.DateTimeField(verbose_name='logout date time')

    def __str__(self):
        return str(self.login_time)

    def get_absolute_url(self):
        return reverse('user_stat_detail', args=[str(self.id)])
