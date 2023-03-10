# Generated by Django 4.1.5 on 2023-01-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_appuser_managers_appuser_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=254, null=True)),
                ('phone', models.PositiveIntegerField()),
                ('department', models.CharField(choices=[('Engineering', 'Engineering'), ('HR', 'HR'), ('Finance', 'Finance')], max_length=50)),
                ('position', models.CharField(max_length=254)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]
