"""Serializers of titles app."""

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from titles.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    """Serializer of category."""

    class Meta:
        """Meta class for serializer of category."""

        model = Category
        fields = ['name', 'slug']


class GenreSerializer(serializers.ModelSerializer):
    """Serializer of genre."""

    class Meta:
        """Meta class for serializer of genre."""
        
        model = Genre
        fields = ['name', 'slug']


class TitleSerializerRead(serializers.ModelSerializer):
    """Serializer of title for reading only."""

    category = CategorySerializer(many=False, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.FloatField(read_only=True)

    class Meta:
        """Meta class for title serializer."""

        model = Title
        fields = '__all__'


class TitleSerializerWrite(serializers.ModelSerializer):
    """Serializer of title for writing."""

    category = SlugRelatedField(
        slug_field='slug', read_only=False,
        queryset=Category.objects.all()
    )
    genre = SlugRelatedField(
        slug_field='slug', read_only=False,
        queryset=Genre.objects.all(),
        many=True
    )

    class Meta:
        """Meta class for title serializer."""
        
        model = Title
        fields = '__all__'
