# Generated by Django 4.2.2 on 2023-07-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_master_wizard_app', '0005_remove_content_uploading_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='title',
            field=models.CharField(default=1),
            preserve_default=False,
        ),
    ]
