# Generated by Django 2.2.7 on 2022-02-24 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0020_financialrequest_payment_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentaccount',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='paymentaccount',
            name='platform',
            field=models.CharField(choices=[('paypal', 'PayPal'), ('payoneer', 'Payoneer'), ('upwork', 'Upwork'), ('freelancer', 'Freelancer'), ('toptal', 'Toptal'), ('binance', 'Binance'), ('metamask', 'MetaMask'), ('bank', 'Bank'), ('usdt', 'USDT'), ('usdc', 'USDC')], max_length=10),
        ),
    ]
