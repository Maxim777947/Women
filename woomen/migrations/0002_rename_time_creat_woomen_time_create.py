# Generated by Django 5.0.7 on 2024-08-10 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('woomen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='woomen',
            old_name='time_creat',
            new_name='time_create',
        ),
    ]