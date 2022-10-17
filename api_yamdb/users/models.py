"""Module with models of users app."""

from xmlrpc.client import Boolean
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

ROLE_USER = 'user'
ROLE_MODERATOR = 'moderator'
ROLE_ADMIN = 'admin'

ROLES = [
    (ROLE_USER, 'Пользователь'),
    (ROLE_MODERATOR, 'Модератор'),
    (ROLE_ADMIN, 'Администратор')
]


class CustomUserManager(UserManager):
    """Custom user manager."""

    def create_user(self, username, email, password, **extra_fields) -> None:
        """User creation."""
        if not email:
            raise ValueError('Email is required')
        if username == 'me':
            raise ValueError('"me" is invalid username')
        return super().create_user(
            username, email=email, password=password, **extra_fields)

    def create_superuser(
            self, username, email, password, role, **extra_fields) -> None:
        """Superuser creation."""
        return super().create_superuser(
            username, email, password, role='admin', **extra_fields)


class User(AbstractUser):
    """Model of user."""

    role = models.CharField(
        choices=ROLES,
        default='user',
        blank=False,
        null=False,
        max_length=200,
        verbose_name='Роль',
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Юзернейм',
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография',
    )
    objects = CustomUserManager()

    REQUIRED_FIELDS = ('email', 'password')

    class Meta:
        """Meta class for model of user."""

        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self) -> Boolean:
        """Get if user object role param is admin."""
        return self.role == ROLES[2][0]

    @property
    def is_moderator(self) -> Boolean:
        """Get if user object role param is moderator."""
        return self.role == ROLES[1][0]


User._meta.get_field('last_name').max_length = 150
User._meta.get_field('first_name').max_length = 150
User._meta.get_field('email').max_length = 254
