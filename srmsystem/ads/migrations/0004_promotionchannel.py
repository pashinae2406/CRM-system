# Generated by Django 5.0.6 on 2024-06-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_ads_profit'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionChannel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
