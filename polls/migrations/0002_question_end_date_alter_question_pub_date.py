# Generated by Django 4.2.4 on 2023-09-09 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date ended'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.localtime, verbose_name='date published'),
        ),
    ]
