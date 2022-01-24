# Generated by Django 2.2.16 on 2022-01-23 20:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220123_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(1, 'минимальная оценка 1'), django.core.validators.MaxLengthValidator(10, 'максимальная оценка 10')], verbose_name='оценка'),
        ),
    ]