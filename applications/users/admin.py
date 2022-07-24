from atexit import register
from curses.ascii import US
from django.contrib import admin

# Register your models here.
from .models import User

admin.site.register(User)