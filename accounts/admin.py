from django.contrib import admin

from .models import Role, UserRole, UserStatistic

models = [Role, UserRole,UserStatistic]
admin.site.register(models)
