# Generated by Django 4.0.4 on 2022-07-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pollapp', '0003_poll_poll_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='votes', to='Pollapp.votes'),
        ),
    ]
