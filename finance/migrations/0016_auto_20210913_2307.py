# Generated by Django 2.2.7 on 2021-09-13 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0015_auto_20210322_0733'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='weakly_limit',
            new_name='weekly_limit',
        ),
    ]