# Generated by Django 4.1.3 on 2023-03-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projement_app', '0002_alter_project_actual_hours_alter_project_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_ended',
            field=models.BooleanField(default=False),
        ),
    ]
