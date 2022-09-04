# Generated by Django 4.1 on 2022-09-04 09:14

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('preview', imagekit.models.fields.ProcessedImageField(upload_to='', verbose_name='Превью для аниме')),
            ],
        ),
    ]
