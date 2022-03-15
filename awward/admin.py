from django.contrib import admin
from .models import User, Project,Rate

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Rate)