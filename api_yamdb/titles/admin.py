"""Module with admin panel configurations."""

from django.contrib import admin

from titles.models import Category, Genre, Title


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin panel configuration for Category model."""

    list_display = ('pk', 'name', 'slug')


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    """Admin panel configuration for Title model."""

    list_display = ('pk', 'name', 'year', 'description',
                    'category')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Admin panel configuration for Genre model."""

    list_display = ('pk', 'name', 'slug')
