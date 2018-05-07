# Generated by Django 2.0.5 on 2018-05-07 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180507_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='updated',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='updated'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='url',
            field=models.URLField(error_messages={'unique': 'This link already exists!'}, unique=True, verbose_name='url'),
        ),
    ]