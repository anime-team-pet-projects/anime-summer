# Generated by Django 4.1 on 2022-09-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0004_anime_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='average_rating',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=10, verbose_name='Средняя оценка'),
        ),
    ]
