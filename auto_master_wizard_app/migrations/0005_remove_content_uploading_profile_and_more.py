# Generated by Django 4.2.2 on 2023-06-25 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auto_master_wizard_app', '0004_rename_uploading_profile_id_content_uploading_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='uploading_profile',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='trims',
        ),
        migrations.RemoveField(
            model_name='trim',
            name='profiles',
        ),
        migrations.AddField(
            model_name='content',
            name='uploaded_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='contents', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='favourites', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trim',
            name='users',
            field=models.ManyToManyField(related_name='favourite_trims', through='auto_master_wizard_app.Favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
