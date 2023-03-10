# Generated by Django 4.1.4 on 2022-12-21 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('YT', 'Youtube'), ('SP', 'Spotify'), ('NF', 'Netflix'), ('AP', 'Amazon Video'), ('ST', 'Start+'), ('PM', 'Paramount+')], default='NF', max_length=2)),
                ('description', models.CharField(max_length=300)),
                ('logo', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
