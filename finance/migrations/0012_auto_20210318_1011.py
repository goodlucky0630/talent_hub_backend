# Generated by Django 2.2.7 on 2021-03-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_financialrequest_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialrequest',
            name='counter_party_id',
        ),
        migrations.RemoveField(
            model_name='financialrequest',
            name='counter_party_type',
        ),
        migrations.AddField(
            model_name='financialrequest',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]