"""Module with admin panel configurations."""

from django.contrib import admin

from reviews.models import Comments, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin panel configuration for Review model."""

    list_display = ('pk', 'text', 'score', 'pub_date', 'title')


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """Admin panel configuration for Comments model."""
    
    list_display = ('pk', 'text', 'author', 'pub_date', 'review')
