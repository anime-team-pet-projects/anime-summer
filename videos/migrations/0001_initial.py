# Generated by Django 4.1 on 2022-09-04 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='', verbose_name='Видео')),
                ('type', models.TextField(choices=[('anime_series', 'Серия аниме')], verbose_name='Тип видео')),
                ('number_video', models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер серии')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
    ]
