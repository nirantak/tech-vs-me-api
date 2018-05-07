# Generated by Django 2.0.5 on 2018-05-07 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180507_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': 'This username already exists!'}, max_length=100, unique=True, verbose_name='username')),
                ('social', models.URLField(error_messages={'unique': 'This link already exists!'}, max_length=255, unique=True, verbose_name='social')),
                ('posts', models.CharField(max_length=250, verbose_name='posts')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
                'ordering': ['id'],
                'get_latest_by': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'get_latest_by': ['updated', 'published'], 'ordering': ['-updated', '-published'], 'verbose_name': 'post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AlterField(
            model_name='posts',
            name='author',
            field=models.CharField(default='nirantak', max_length=250, verbose_name='author'),
        ),
    ]