# Generated by Django 2.2.7 on 2021-02-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0008_auto_20210131_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='weakly_limit',
            field=models.IntegerField(blank=True, default=40, null=True),
        ),
    ]