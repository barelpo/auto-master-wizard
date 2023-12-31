# Generated by Django 4.2.2 on 2023-06-24 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_master_wizard_app', '0002_rename_favorite_favourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='trims',
            field=models.ManyToManyField(related_name='favourite_profiles', through='auto_master_wizard_app.Favourite', to='auto_master_wizard_app.trim'),
        ),
        migrations.AddField(
            model_name='trim',
            name='profiles',
            field=models.ManyToManyField(related_name='favourite_trims', through='auto_master_wizard_app.Favourite', to='auto_master_wizard_app.profile'),
        ),
    ]
