"""Module with admin panel configurations."""

from django.contrib import admin

from users.models import User

admin.site.register(User)
