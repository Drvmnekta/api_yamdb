from django.db import models
from pytils.translit import slugify


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Категория')
    slug = models.SlugField(max_length=50, unique=True, blank=True,)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        super().save(*args, **kwargs)        


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='Жанр')
    slug = models.SlugField(max_length=50, unique=True, blank=True,)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name[:50]


class Title(models.Model):
    name = models.CharField(
        max_length=256, verbose_name='Название',
        blank=False, null=False
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        blank=True, null=True
    )
    raiting = models.IntegerField(
        verbose_name='Рейтинг',
        blank=True, null=True
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='category'
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='genre'
    )

    def __str__(self):
        return self.name[:50]


class TitleGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} {self.genre}'
