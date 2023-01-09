# Generated by Django 2.2.7 on 2022-03-24 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0022_auto_20220312_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='payment_period',
            field=models.IntegerField(blank=True, choices=[(1, 'Weekly'), (2, 'Bi-Weekly'), (3, 'Monthly')], default=1, null=True),
        ),
    ]