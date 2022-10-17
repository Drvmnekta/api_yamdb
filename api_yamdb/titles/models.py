"""Module with models of titles app."""

import datetime as dt

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


def current_year() -> dt.date:
    """Get current year."""
    return dt.date.today().year


class Category(models.Model):
    """Model of category."""

    name = models.CharField(max_length=256, verbose_name='Категория')
    slug = models.SlugField(max_length=50, unique=True, blank=True,)

    class Meta:
        """Meta class for model of category."""

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        """Get string representation of category object."""
        return self.name

    def save(self, *args, **kwargs) -> None:
        """Save category object."""
        if not self.slug:
            self.slug = slugify(self.name[:50])
        super().save(*args, **kwargs)


class Genre(models.Model):
    """Model of genre."""

    name = models.CharField(max_length=256, verbose_name='Жанр')
    slug = models.SlugField(max_length=50, unique=True, blank=True,)

    class Meta:
        """Meta class for model of genre."""

        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        """Get string representation of genre object."""
        return self.name[:50]

    def save(self, *args, **kwargs) -> None:
        """Save genre object."""
        if not self.slug:
            self.slug = slugify(self.name[:50])
        super().save(*args, **kwargs)


class Title(models.Model):
    """Model of title."""

    name = models.CharField(
        max_length=256,
        verbose_name='Название',
        blank=False,
        null=False
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(current_year())]
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='category',
        verbose_name='Категория',
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
    )

    class Meta:
        """Meta class for model of title."""

        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self) -> str:
        """Get string representation of title object."""
        return self.name[:50]
