# Generated by Django 4.0.4 on 2022-08-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pollapp', '0005_poll_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
