# Generated by Django 2.2.7 on 2021-09-18 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20210915_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Team'),
        ),
    ]