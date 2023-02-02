# Generated by Django 4.1.5 on 2023-01-24 08:40

import assignment.web.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_appuser_groups_appuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
                ('objects', assignment.web.managers.AppUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='appuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]